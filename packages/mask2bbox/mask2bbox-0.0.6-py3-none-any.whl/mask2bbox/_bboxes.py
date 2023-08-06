# =============================================================================
# Import third-party libraries
from numpy import ndarray
from skimage import io
import numpy as np
from matplotlib import pyplot as plt


# Create a bbox class
class BBoxes:
    """Class to calculate and represent bounding boxes from a mask file"""
    n: int
    bbox: np.ndarray

    # Constructor
    def __init__(self, mask_file):
        # Read in the mask file
        self.mask = io.imread(mask_file)

        # Get the shape of the mask image
        self.mask_shape = self.mask.shape

        # Get the bounding boxes
        self.bboxes = self._get_bboxes()

    def __len__(self) -> int:
        return self.bboxes.shape[0]

    def _get_bboxes(self) -> np.ndarray:
        """
        Calculates the bounding boxes from the mask file.
        :return: A numpy array with the bounding boxes.
        """
        # Get indexes of nonzero elements
        nonzero = np.array(np.nonzero(self.mask)).T

        # Get cell identities of nonzero matrix
        identities = np.array(list(map(lambda x: self.mask[x[0]][x[1]], nonzero)))

        # Stack identities with the nonzero matrix
        stacked = np.column_stack((identities, nonzero))

        # sort them by identity
        stacked = stacked[stacked[:, 0].argsort()]

        # Group them by identity
        grouped = np.split(stacked[:, 1:], np.unique(stacked[:, 0], return_index=True)[1][1:])

        # Get the bounding boxes for each identity
        bboxes = np.array(list(map(lambda x: np.array([min(x[:, 0]), max(x[:, 0]), min(x[:, 1]), max(x[:, 1])]),
                                   np.array(grouped, dtype=object))))

        # Since the bounding boxes are calculated from the group identities we can add column with the identities
        bboxes = np.column_stack((np.unique(stacked[:, 0]), bboxes))

        # Return the bounding boxes
        return bboxes

    def expand(self, n) -> None:
        # Expand the bounding boxes by n pixels, but not beyond the image size.
        self.bboxes = np.array(list(map(lambda x: np.array([x[0],
                                                            max(x[1] - n, 0),
                                                            min(x[2] + n, self.mask_shape[0]),
                                                            max(x[3] - n, 0),
                                                            min(x[4] + n, self.mask_shape[1])]), self.bboxes)))

    def remove_edge_boxes(self) -> None:
        # Removes the bonds that are on the edge of the image
        self.bboxes = self.bboxes[np.where((self.bboxes[:, 1] > 0) &
                                           (self.bboxes[:, 2] < self.mask_shape[0]) &
                                           (self.bboxes[:, 3] > 0) &
                                           (self.bboxes[:, 4] < self.mask_shape[1]))]

    def get_bbox_dims(self) -> np.ndarray:
        # Get the sides of the bounding boxes
        return np.array([self.bboxes[:, 0],
                         self.bboxes[:, 2] - self.bboxes[:, 1],
                         self.bboxes[:, 4] - self.bboxes[:, 3]]).T

    def get_bbox_areas(self) -> np.ndarray:
        # Get the areas of the bounding boxes
        return np.array([self.bboxes[:, 0],
                         (self.bboxes[:, 2] - self.bboxes[:, 1]) *
                         (self.bboxes[:, 4] - self.bboxes[:, 3])]).T

    def get_bbox_ratios(self) -> np.ndarray:
        # Get the aspect ratios of the bounding boxes
        ratios = np.array((self.bboxes[:, 2] - self.bboxes[:, 1]) / (self.bboxes[:, 4] - self.bboxes[:, 3]))

        return np.array(([self.bboxes[:, 0], ratios]))

    def get_bbox_centers(self) -> np.ndarray:
        # Get the centers of the bounding boxes
        return np.array([self.bboxes[:, 0],
                         (self.bboxes[:, 2] + self.bboxes[:, 1]) // 2,
                         (self.bboxes[:, 4] + self.bboxes[:, 3]) // 2]).T

    def is_area_smaller_than(self, area) -> ndarray:
        # Get areas of the bounding boxes
        areas = self.get_bbox_areas()

        # Get the identities of the bounding boxes that have an area smaller than the area parameter
        identities = areas[np.where(areas[:, 1] < area)[0], 0]

        return identities

    def is_area_larger_than(self, area) -> ndarray:
        # Get areas of the bounding boxes
        areas = self.get_bbox_areas()

        # Get the identities of the bounding boxes that have an area bigger than the area parameter
        identities = areas[np.where(areas[:, 1] >= area)[0], 0]

        return identities

    def are_dims_smaller_than(self, dims) -> ndarray:
        # Get dimensions of the bounding boxes
        dimensions = self.get_bbox_dims()

        # Get the identities of the bounding boxes that have a dimension smaller than the dims parameter
        identities = dimensions[np.where((dimensions[:, 1] < dims[0]) & (dimensions[:, 2] < dims[1]))[0], 0]

        return identities

    def are_dims_larger_than(self, dims) -> np.ndarray:
        # Get dimensions of the bounding boxes
        dimensions = self.get_bbox_dims()

        # Get the identities of the bounding boxes that have a dimension bigger than the dims parameter
        identities = dimensions[np.where((dimensions[:, 1] >= dims[0]) & (dimensions[:, 2] > dims[1]))[0], 0]

        return identities

    def filter_identities(self, identities) -> None:
        # Get only the bounding boxes of the specific identity
        self.bboxes = self.bboxes[np.where(np.isin(self.bboxes[:, 0], identities))]

    def plot_to_mask(self, output_file=None) -> None:
        # Get the ratio of the mask
        mask_ratio = self.mask_shape[0] / self.mask_shape[1]

        # Draw the bounding boxes on the mask
        fig, ax = plt.subplots(1, 1, figsize=(10, mask_ratio * 10))
        ax.imshow(self.mask, cmap="gray")

        # Draw the bounding boxes
        for bbox in self.bboxes:
            ax.plot([bbox[3], bbox[4]], [bbox[1], bbox[1]], color="red")  # Top
            ax.plot([bbox[3], bbox[4]], [bbox[2], bbox[2]], color="red")  # Bottom
            ax.plot([bbox[3], bbox[3]], [bbox[1], bbox[2]], color="red")  # Left
            ax.plot([bbox[4], bbox[4]], [bbox[1], bbox[2]], color="red")  # Right
        ax.axis("off")
        fig.tight_layout()

        # If not path is given, show the plot
        if output_file is not None:
            plt.savefig(output_file)
        else:
            plt.show()

    @staticmethod
    def iou(box1, box2) -> float:
        # Calculate the intersection box
        x1 = max(box1[1], box2[1])
        x2 = min(box1[2], box2[2])
        y1 = max(box1[3], box2[3])
        y2 = min(box1[4], box2[4])

        # Calculate intersection area
        intersection = max(0, x2 - x1) * max(0, y2 - y1)

        # Calculate union area
        area1 = (box1[3] - box1[1]) * (box1[4] - box1[2])
        area2 = (box2[3] - box2[1]) * (box2[4] - box2[2])
        union = area1 + area2 - intersection

        # Calculate and return IoU
        return intersection / union

    @property
    def iou_matrix(self) -> ndarray:
        n = self.__len__()
        # compute the size of the matrix based on the length of the array
        size = n * (n - 1) // 2

        # create a 1D array of zeros to hold the upper triangular matrix
        triangular = np.zeros(size)

        # fill the upper triangular matrix with elements from the original array
        k = 0
        for i in range(n):
            for j in range(i + 1, n):
                triangular[k] = self.iou(self.bboxes[i], self.bboxes[j])
                k += 1

        # convert the 1D array to a 2D matrix
        matrix: ndarray = np.zeros((n, n))
        matrix[np.triu_indices(n, k=1)] = triangular

        return matrix

    def are_overlapping(self) -> ndarray:
        # Get the IoU matrix
        overlapping = np.where(self.iou_matrix > 0)

        # Get the identities from the overlapping indexes
        identities = self.bboxes[np.unique(overlapping), 0]

        return identities

    def overlapping_pairs(self) -> (ndarray, ndarray):
        # Get the IoU matrix
        iou_matrix = self.iou_matrix

        # Get elements that are not zero
        x, y = np.where(iou_matrix > 0)
        v = iou_matrix[x, y]
        x = self.bboxes[x, 0]
        y = self.bboxes[y, 0]

        return np.array([x, y]).T, v

    def save_iou(self, output_file: str) -> None:
        # Save the IoU matrix to a csv file
        np.savetxt(output_file, self.iou_matrix, delimiter=",")

    def save_csv(self, output_file: str) -> None:
        # Save the bounding boxes to a csv file
        np.savetxt(output_file, self.bboxes, delimiter=",", fmt="%d")
