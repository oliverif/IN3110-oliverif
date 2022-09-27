"""numpy implementation of image filters"""

from typing import Optional
import numpy as np

PIXEL_WEIGHTS = np.asarray([0.21, 0.72, 0.07])


def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    gray_image = np.empty_like(image)

    # This one is a lot faster, but I assume np.sum use cython or something under the hood, so it defeats the purpose of
    # this exercise.
    # gray_image[:, :][:] = np.sum(image * PIXEL_WEIGHTS, axis=2, keepdims=True, dtype=np.uint8)

    # iterate through the pixels, and apply the grayscale transform
    for i in range(len(image)):
        for j in range(len(image[i])):
            gray_image[i, j, :] = sum(image[i, j][:] * PIXEL_WEIGHTS)

    # Return image (make sure it's the right type!)
    return gray_image


def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia filter to apply (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    (note: implementing 'k' is a bonus task,
    you may ignore it for Task 9)

    Returns:
        np.array: sepia_image
    """

    if not 0 <= k <= 1:
        # validate k (optional)
        raise ValueError(f"k must be between [0-1], got {k=}")

    sepia_image = ...

    # define sepia matrix (optional: with `k` tuning parameter for bonus task 13)
    sepia_matrix = ...

    # HINT: For version without adaptive sepia filter, use the same matrix as in the pure python implementation
    # use Einstein sum to apply pixel transform matrix
    # Apply the matrix filter
    sepia_image = ...

    # Check which entries have a value greater than 255 and set it to 255 since we can not display values bigger than 255
    ...

    # Return image (make sure it's the right type!)
    return sepia_image
