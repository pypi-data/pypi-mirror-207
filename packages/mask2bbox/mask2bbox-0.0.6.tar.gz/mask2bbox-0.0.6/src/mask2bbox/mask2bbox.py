# Import libraries
import time
import argparse
from _bboxes import BBoxes
from pathlib import Path
import matplotlib.pyplot as plt

# Import third-party libraries
from skimage import io, exposure, transform, restoration
# from aicsimageio import AICSImage
import numpy as np
from tqdm import tqdm


# Get arguments
def get_arguments():
    # Start with the description
    description = "Converts all the masks in a folder to bounding boxes."

    # Add parser
    parser = argparse.ArgumentParser(description=description)

    # Add a group of arguments for input
    input = parser.add_argument_group(title="Input", description="Input arguments for the script.")
    input.add_argument("-m", "--mask", dest="mask", action="store", type=str, required=True,
                       help="Path to the mask file.")

    # Add a group of arguments with the tool options
    options = parser.add_argument_group(title="Options", description="Options for the script.")
    options.add_argument("-e", "--expand", dest="expand", action="store", type=int, required=False, default=0,
                         help="Number of pixels to expand the bounding boxes.")
    options.add_argument("-fs", "--filter-small", dest="filter_small", action="store", type=int, required=False,
                         default=0, help="Filter bounding boxes smaller than the provided value [default=0].")
    options.add_argument("-fl", "--filter-large", dest="filter_large", action="store", type=int, required=False,
                         default=0, help="Filter bounding boxes larger than the provided value [default=0].")
    options.add_argument("-r", "--remove-edge", dest="remove_edge", action="store_true", required=False,
                         default=False, help="Remove bounding boxes that are on the edge of the image.")

    # Add a group of arguments for output
    output = parser.add_argument_group(title="Output", description="Output arguments for the script.")
    output.add_argument("-o", "--output", dest="output", action="store", type=str, required=True,
                        help="Path to the output file with the bounding boxes.")
    output.add_argument("-p", "--plot", dest="plot", action="store", type=str, required=False, default=None,
                        help="Path to the output file with the bounding boxes.")
    output.add_argument("-iou" "--save-iou", dest="save_iou", action="store", type=str, required=False, default=None,
                        help="Path to the output file for the intersection over union (IoU) matrix.")

    # Parse arguments
    args = parser.parse_args()

    # Standardize paths
    args.mask = Path(args.mask).resolve()
    args.output = Path(args.output).resolve()
    args.plot = Path(args.plot).resolve() if args.plot is not None else None

    # Return arguments
    return args


def main(args):
    # Create a BBoxes object and get the bounding boxes
    mask_boxes = BBoxes(args.mask)
    print(f"Total number of bounding boxes     = {mask_boxes.n}")

    # Expand the bounding boxes
    mask_boxes.expand(n=args.expand)
    print(f"Expanding bounding boxes by        = {args.expand}")

    # Filter small bounding boxes
    if args.filter_small > 0:
        print(f"Keeping bounding boxes smaller than = ({args.filter_small}x{args.filter_small})")
        mask_boxes.filter_identities(mask_boxes.are_dims_smaller_than((args.filter_small, args.filter_small)))

    # Filter large bounding boxes
    if args.filter_large > 0:
        print(f"Keeping bounding boxes larger than = ({args.filter_large}x{args.filter_large})")
        mask_boxes.filter_identities(mask_boxes.are_dims_larger_than((args.filter_large, args.filter_large)))

    # Remove bounding boxes on the edge
    if args.remove_edge:
        print("Removing bounding boxes on the edge")
        mask_boxes.remove_edge_boxes()

    # Plot bounding boxes
    if args.plot is not None:
        print(f"Saving plot to                    = {args.plot}")
        mask_boxes.plot_to_mask(args.plot)

    # Save IoU matrix
    if args.save_iou is not None:
        print(f"Saving IoU matrix to              = {args.save_iou}")
        mask_boxes.save_iou(args.save_iou)

    # Save file
    print(f"Saving bounding boxes to           = {args.output}")
    print(f"Number of bounding boxes saved:    = {mask_boxes.n}")
    mask_boxes.save_csv(args.output)


# Run main
if __name__ == "__main__":
    # Get arguments
    args = get_arguments()

    # Run main and time it
    st = time.time()
    main(args)
    rt = time.time() - st
    print(f"Script finish in {rt // 60:.0f}m {rt % 60:.0f}s")