# mask2bbox
[![PyPI](https://img.shields.io/pypi/v/mask2bbox?style=flat-square)](https://pypi.org/project/mask2bbox/)

For a given mask, gets the coordinates of bounding box of each element of the mask. It will also allow for more operations in the future.

## Instalation

`pip install mask2bbox`

## Usage

```python
from mask2bbox import BBoxes

# Create a BBoxes object
all_boxes = BBoxes("path/to/mask.png")

# Expand the bounding boxes
all_boxes.expand(n=10)

# Remove the bounding boxes that are located on the edge of the image
all_boxes.remove_edge_boxes()

# Get the area of all the bounding boxes
araa = all_boxes.get_bbox_areas()

# Get the dimensions on x and y of all the bounding boxes
dims = all_boxes.get_bbox_dims()

# Get the center of all the bounding boxes
centers = all_boxes.get_bbox_centers()

# Get the ratio x/y of all the bounding boxes
ratios = all_boxes.get_bbox_ratios()

# Get the IoU matrix of all the bounding boxes
iou = all_boxes.iou_matrix()

# Save the IoU matrix to a csv file
all_boxes.save_iou("path/to/save/iou.csv")

# Plot the bounding boxes on the mask image
all_boxes.plot_to_mask("path/to/save/image.png")

# Save your bounding boxes
all_boxes.save_csv("path/to/bounding_boxes.csv")
```

## Version Notes

### 0.0.5 - Added functionality

- IoU related operations:
  - `boxes.get_iou_matrix()` - Gets the IoU of all the bounding boxes.
  - `boxes.are_overlaping()` - Returns identities where the IoU is greater than 0
  - `boxes.overlaping_pais()` - Returns the pairs of bounding boxes that are overlaping.
  - `boxes.save_iou()` - Saves the IoU matrix to a csv file.

- Plots
  - `boxes.plot_to_mask()` Plots the bounding boxes on the mask image.

Example of `boxes.plot_to_mask()` where only the overlapping bounding boxes are highlighted.
![](tests/plot.png)

### 0.0.4 - Added functionality
Now is possible to extract:
- Bounding boxes dimensions `BBoxes.get_bbox_dims()`
- Bounding boxes area `BBoxes.get_bbox_areas()`
- Bounding boxes center `BBoxes.get_bbox_centers()`
- Bounding boxes ratios `BBoxes.get_bbox_ratios()`

### 0.0.3 - Added functionality  
Added the remove_edge_boxes method to remove the bounding boxes that are located on the edge of the image.

### 0.0.2 - Added the expand method to expand the bounding boxes by a given number of pixels.
Added the expand method to expand the bounding boxes by a given number of pixels.  
Fixed a bug in the setup.py file that made it hard to import the package.

### 0.0.1 - Initial release of the package.
Initial release of the package. It allows to get the bounding boxes of a mask and save them to a csv file.
