"""
The source code is adapted from https://github.com/aliaksandr960/segment-anything-eo. Credit to the author Aliaksandr Hancharenka.
"""

import os
import cv2
import torch
import numpy as np
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor
from segment_anything.utils.transforms import ResizeLongestSide

from .common import *


class SamGeo:
    """The main class for segmenting geospatial data with the Segment Anything Model (SAM). See
    https://github.com/facebookresearch/segment-anything
    """

    def __init__(
        self,
        model_type="vit_h",
        checkpoint="sam_vit_h_4b8939.pth",
        automatic=True,
        device=None,
        erosion_kernel=None,
        mask_multiplier=255,
        sam_kwargs=None,
    ):
        """Initialize the class.

        Args:
            model_type (str, optional): The model type. It can be one of the following: vit_h, vit_l, vit_b.
                Defaults to 'vit_h'. See https://bit.ly/3VrpxUh for more details.
            checkpoint (str, optional): The path to the checkpoint. It can be one of the following:
                sam_vit_h_4b8939.pth, sam_vit_l_0b3195.pth, sam_vit_b_01ec64.pth.
                Defaults to "sam_vit_h_4b8939.pth". See https://bit.ly/3VrpxUh for more details.
            automatic (bool, optional): Whether to use the automatic mask generator or input prompts. Defaults to True.
                The automatic mask generator will segment the entire image, while the input prompts will segment selected objects.
            device (str, optional): The device to use. It can be one of the following: cpu, cuda.
                Defaults to None, which will use cuda if available.
            erosion_kernel (tuple, optional): The erosion kernel for filtering object masks and extract borders.
                Set to None to disable it. Defaults to (3, 3).
            mask_multiplier (int, optional): The mask multiplier for the output mask, which is usually a binary mask [0, 1].
                You can use this parameter to scale the mask to a larger range, for example [0, 255]. Defaults to 255.
            sam_kwargs (dict, optional): Optional arguments for fine-tuning the SAM model. Defaults to None.
                The available arguments with default values are listed below. See https://bit.ly/410RV0v for more details.

                points_per_side: Optional[int] = 32,
                points_per_batch: int = 64,
                pred_iou_thresh: float = 0.88,
                stability_score_thresh: float = 0.95,
                stability_score_offset: float = 1.0,
                box_nms_thresh: float = 0.7,
                crop_n_layers: int = 0,
                crop_nms_thresh: float = 0.7,
                crop_overlap_ratio: float = 512 / 1500,
                crop_n_points_downscale_factor: int = 1,
                point_grids: Optional[List[np.ndarray]] = None,
                min_mask_region_area: int = 0,
                output_mode: str = "binary_mask",

        """
        # Download the checkpoint if it does not exist
        if not os.path.exists(checkpoint):
            print(f"Checkpoint {checkpoint} does not exist.")
            download_checkpoint(output=checkpoint)

        # Use cuda if available
        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"

        self.checkpoint = checkpoint
        self.model_type = model_type
        self.device = device
        self.sam_kwargs = sam_kwargs  # Optional arguments for fine-tuning the SAM model
        self.source = None  # Store the input image path
        self.image = None  # Store the input image as a numpy array
        # Store the masks as a list of dictionaries. Each mask is a dictionary
        # containing segmentation, area, bbox, predicted_iou, point_coords, stability_score, and crop_box
        self.masks = None
        self.objects = None  # Store the mask objects as a numpy array
        # Store the annotations (objects with random color) as a numpy array.
        self.annotations = None

        # Build the SAM model
        self.sam = sam_model_registry[self.model_type](checkpoint=self.checkpoint)
        self.sam.to(device=self.device)
        # Use optional arguments for fine-tuning the SAM model
        sam_kwargs = self.sam_kwargs if self.sam_kwargs is not None else {}

        if automatic:
            # Segment the entire image using the automatic mask generator
            self.mask_generator = SamAutomaticMaskGenerator(self.sam, **sam_kwargs)
        else:
            # Segment selected objects using input prompts
            self.predictor = SamPredictor(self.sam, **sam_kwargs)

        # Apply the erosion filter to the mask to extract borders
        self.erosion_kernel = erosion_kernel
        if self.erosion_kernel is not None:
            self.erosion_kernel = np.ones(erosion_kernel, np.uint8)

        # Rescale the binary mask to a larger range, for example, from [0, 1] to [0, 255].
        self.mask_multiplier = mask_multiplier

    def __call__(self, image):
        # Segment each image tile
        h, w, _ = image.shape

        masks = self.mask_generator.generate(image)

        resulting_mask = np.ones((h, w), dtype=np.uint8)
        resulting_borders = np.zeros((h, w), dtype=np.uint8)

        for m in masks:
            mask = (m["segmentation"] > 0).astype(np.uint8)
            resulting_mask += mask

            # Apply erosion to the mask
            if self.erosion_kernel is not None:
                mask_erode = cv2.erode(mask, self.erosion_kernel, iterations=1)
                mask_erode = (mask_erode > 0).astype(np.uint8)
                edge_mask = mask - mask_erode
                resulting_borders += edge_mask

        resulting_mask = (resulting_mask > 0).astype(np.uint8)
        resulting_borders = (resulting_borders > 0).astype(np.uint8)
        resulting_mask_with_borders = resulting_mask - resulting_borders
        return resulting_mask_with_borders * self.mask_multiplier

    def generate(
        self,
        source,
        output=None,
        foreground=True,
        batch=False,
        erosion_kernel=None,
        mask_multiplier=255,
        unique=True,
        **kwargs,
    ):
        """Generate masks for the input image.

        Args:
            source (str | np.ndarray): The path to the input image or the input image as a numpy array.
            output (str, optional): The path to the output image. Defaults to None.
            foreground (bool, optional): Whether to generate the foreground mask. Defaults to True.
            batch (bool, optional): Whether to generate masks for a batch of image tiles. Defaults to False.
            erosion_kernel (tuple, optional): The erosion kernel for filtering object masks and extract borders.
                Such as (3, 3) or (5, 5). Set to None to disable it. Defaults to None.
            mask_multiplier (int, optional): The mask multiplier for the output mask, which is usually a binary mask [0, 1].
                You can use this parameter to scale the mask to a larger range, for example [0, 255]. Defaults to 255.
                The parameter is ignored if unique is True.
            unique (bool, optional): Whether to assign a unique value to each object. Defaults to True.
                The unique value increases from 1 to the number of objects. The larger the number, the larger the object area.

        """

        if isinstance(source, str):
            if source.startswith("http"):
                source = download_file(source)

            if not os.path.exists(source):
                raise ValueError(f"Input path {source} does not exist.")

            if batch:  # Subdivide the image into tiles and segment each tile
                return tiff_to_tiff(source, output, self, **kwargs)

            image = cv2.imread(source)
        elif isinstance(source, np.ndarray):
            image = source
        else:
            raise ValueError("Input source must be either a path or a numpy array.")

        self.source = source  # Store the input image path
        self.image = image  # Store the input image as a numpy array
        mask_generator = self.mask_generator  # The automatic mask generator
        masks = mask_generator.generate(image)  # Segment the input image
        self.masks = masks  # Store the masks as a list of dictionaries

        if output is not None:
            # Save the masks to the output path. The output is either a binary mask or a mask of objects with unique values.
            self.save_masks(
                output, foreground, unique, erosion_kernel, mask_multiplier, **kwargs
            )

    def save_masks(
        self,
        output=None,
        foreground=True,
        unique=True,
        erosion_kernel=None,
        mask_multiplier=255,
        **kwargs,
    ):
        """Save the masks to the output path. The output is either a binary mask or a mask of objects with unique values.

        Args:
            output (str, optional): The path to the output image. Defaults to None, saving the masks to SamGeo.objects.
            foreground (bool, optional): Whether to generate the foreground mask. Defaults to True.
            unique (bool, optional): Whether to assign a unique value to each object. Defaults to True.
            erosion_kernel (tuple, optional): The erosion kernel for filtering object masks and extract borders.
                Such as (3, 3) or (5, 5). Set to None to disable it. Defaults to None.
            mask_multiplier (int, optional): The mask multiplier for the output mask, which is usually a binary mask [0, 1].
                You can use this parameter to scale the mask to a larger range, for example [0, 255]. Defaults to 255.

        """

        if self.masks is None:
            raise ValueError("No masks found. Please run generate() first.")

        h, w, _ = self.image.shape
        masks = self.masks

        # Set output image data type based on the number of objects
        if len(masks) < 255:
            dtype = np.uint8
        elif len(masks) < 65535:
            dtype = np.uint16
        else:
            dtype = np.uint32

        # Generate a mask of objects with unique values
        if unique:
            # Sort the masks by area in ascending order
            sorted_masks = sorted(masks, key=(lambda x: x["area"]), reverse=False)

            # Create an output image with the same size as the input image
            objects = np.zeros(
                (
                    sorted_masks[0]["segmentation"].shape[0],
                    sorted_masks[0]["segmentation"].shape[1],
                )
            )
            # Assign a unique value to each object
            for index, ann in enumerate(sorted_masks):
                m = ann["segmentation"]
                objects[m] = index + 1

        # Generate a binary mask
        else:
            if foreground:  # Extract foreground objects only
                resulting_mask = np.zeros((h, w), dtype=dtype)
            else:
                resulting_mask = np.ones((h, w), dtype=dtype)
            resulting_borders = np.zeros((h, w), dtype=dtype)

            for m in masks:
                mask = (m["segmentation"] > 0).astype(dtype)
                resulting_mask += mask

                # Apply erosion to the mask
                if erosion_kernel is not None:
                    mask_erode = cv2.erode(mask, erosion_kernel, iterations=1)
                    mask_erode = (mask_erode > 0).astype(dtype)
                    edge_mask = mask - mask_erode
                    resulting_borders += edge_mask

            resulting_mask = (resulting_mask > 0).astype(dtype)
            resulting_borders = (resulting_borders > 0).astype(dtype)
            objects = resulting_mask - resulting_borders
            objects = objects * mask_multiplier

        objects = objects.astype(dtype)
        self.objects = objects

        if output is not None:  # Save the output image
            array_to_image(self.objects, output, self.source, **kwargs)

    def show_masks(
        self, figsize=(12, 10), cmap="binary_r", axis="off", foreground=True, **kwargs
    ):
        """Show the binary mask or the mask of objects with unique values.

        Args:
            figsize (tuple, optional): The figure size. Defaults to (12, 10).
            cmap (str, optional): The colormap. Defaults to "binary_r".
            axis (str, optional): Whether to show the axis. Defaults to "off".
            foreground (bool, optional): Whether to show the foreground mask only. Defaults to True.
        """

        import matplotlib.pyplot as plt

        if self.objects is None:
            self.save_masks(foreground=foreground, **kwargs)

        plt.figure(figsize=figsize)
        plt.imshow(self.objects, cmap=cmap)
        plt.axis(axis)
        plt.show()

    def show_anns(
        self, figsize=(12, 10), axis="off", alpha=0.35, output=None, **kwargs
    ):
        """Show the annotations (objects with random color) on the input image.

        Args:
            figsize (tuple, optional): The figure size. Defaults to (12, 10).
            axis (str, optional): Whether to show the axis. Defaults to "off".
            alpha (float, optional): The alpha value for the annotations. Defaults to 0.35.
            output (str, optional): The path to the output image. Defaults to None.
        """

        import matplotlib.pyplot as plt

        anns = self.masks

        if self.image is None:
            print("Please run generate() first.")
            return

        if anns is None or len(anns) == 0:
            return

        plt.figure(figsize=figsize)
        plt.imshow(self.image)

        sorted_anns = sorted(anns, key=(lambda x: x["area"]), reverse=True)

        ax = plt.gca()
        ax.set_autoscale_on(False)

        img = np.ones(
            (
                sorted_anns[0]["segmentation"].shape[0],
                sorted_anns[0]["segmentation"].shape[1],
                4,
            )
        )
        img[:, :, 3] = 0
        for ann in sorted_anns:
            m = ann["segmentation"]
            color_mask = np.concatenate([np.random.random(3), [alpha]])
            img[m] = color_mask
        ax.imshow(img)

        if "dpi" not in kwargs:
            kwargs["dpi"] = 100

        if "bbox_inches" not in kwargs:
            kwargs["bbox_inches"] = "tight"

        plt.axis(axis)

        self.annotations = (img[:, :, 0:3] * 255).astype(np.uint8)

        if output is not None:
            array = blend_images(self.annotations, self.image, alpha=alpha, show=False)
            array_to_image(array, output, self.source)

    def predict(self, in_path, out_path, prompts, image_format="RGB", **kwargs):
        """Segment the input image and save the result to the output path.

        Args:
            in_path (str): The path to the input image.
            out_path (str): The path to the output image.
            prompts (list): The prompts to use.
        """
        predictor = self.predictor
        predictor.set_image(in_path, image_format=image_format)
        masks, _, _ = predictor.predict(prompts, **kwargs)
        return masks

    def image_to_image(self, image, **kwargs):
        return image_to_image(image, self, **kwargs)

    def download_tms_as_tiff(self, source, pt1, pt2, zoom, dist):
        image = draw_tile(source, pt1[0], pt1[1], pt2[0], pt2[1], zoom, dist)
        return image

    def tiff_to_vector(self, tiff_path, output, simplify_tolerance=None, **kwargs):
        """Convert a tiff file to a gpkg file.

        Args:
            tiff_path (str): The path to the tiff file.
            output (str): The path to the vector file.
            simplify_tolerance (float, optional): The maximum allowed geometry displacement.
                The higher this value, the smaller the number of vertices in the resulting geometry.
        """

        tiff_to_vector(
            tiff_path, output, simplify_tolerance=simplify_tolerance, **kwargs
        )

    def tiff_to_gpkg(self, tiff_path, output, simplify_tolerance=None, **kwargs):
        """Convert a tiff file to a gpkg file.

        Args:
            tiff_path (str): The path to the tiff file.
            output (str): The path to the gpkg file.
            simplify_tolerance (float, optional): The maximum allowed geometry displacement.
                The higher this value, the smaller the number of vertices in the resulting geometry.
        """

        tiff_to_gpkg(tiff_path, output, simplify_tolerance=simplify_tolerance, **kwargs)

    def tiff_to_shp(self, tiff_path, output, simplify_tolerance=None, **kwargs):
        """Convert a tiff file to a shapefile.

        Args:
            tiff_path (str): The path to the tiff file.
            output (str): The path to the shapefile.
            simplify_tolerance (float, optional): The maximum allowed geometry displacement.
                The higher this value, the smaller the number of vertices in the resulting geometry.
        """

        tiff_to_shp(tiff_path, output, simplify_tolerance=simplify_tolerance, **kwargs)

    def tiff_to_geojson(self, tiff_path, output, simplify_tolerance=None, **kwargs):
        """Convert a tiff file to a GeoJSON file.

        Args:
            tiff_path (str): The path to the tiff file.
            output (str): The path to the GeoJSON file.
            simplify_tolerance (float, optional): The maximum allowed geometry displacement.
                The higher this value, the smaller the number of vertices in the resulting geometry.
        """

        tiff_to_geojson(
            tiff_path, output, simplify_tolerance=simplify_tolerance, **kwargs
        )


class SamGeoPredictor(SamPredictor):
    def __init__(
        self,
        sam_model,
    ):
        self.model = sam_model
        self.transform = ResizeLongestSide(sam_model.image_encoder.img_size)

    def set_image(self, image):
        super(SamGeoPredictor, self).set_image(image)

    def predict(
        self,
        src_fp=None,
        geo_box=None,
        point_coords=None,
        point_labels=None,
        box=None,
        mask_input=None,
        multimask_output=True,
        return_logits=False,
    ):
        if geo_box and src_fp:
            self.crs = "EPSG:4326"
            dst_crs = get_crs(src_fp)
            sw = transform_coords(geo_box[0], geo_box[1], self.crs, dst_crs)
            ne = transform_coords(geo_box[2], geo_box[3], self.crs, dst_crs)
            xs = np.array([sw[0], ne[0]])
            ys = np.array([sw[1], ne[1]])
            box = get_pixel_coords(src_fp, xs, ys)
            self.geo_box = geo_box
            self.width = box[2] - box[0]
            self.height = box[3] - box[1]
            self.geo_transform = set_transform(geo_box, self.width, self.height)

        masks, iou_predictions, low_res_masks = super(SamGeoPredictor, self).predict(
            point_coords, point_labels, box, mask_input, multimask_output, return_logits
        )

        return masks, iou_predictions, low_res_masks

    def masks_to_geotiff(self, src_fp, dst_fp, masks):
        profile = get_profile(src_fp)
        write_raster(
            dst_fp,
            masks,
            profile,
            self.width,
            self.height,
            self.geo_transform,
            self.crs,
        )

    def geotiff_to_geojson(self, src_fp, dst_fp, bidx=1):
        gdf = get_features(src_fp, bidx)
        write_features(gdf, dst_fp)
        return gdf
