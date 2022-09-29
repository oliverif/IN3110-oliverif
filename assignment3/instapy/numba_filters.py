"""numba-optimized filters"""
from numba import jit
import numpy as np


@jit(nopython=True)
def numba_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    COLOR_WEIGHTS = [0.21, 0.72, 0.07]
    gray_image = np.empty_like(image)
    """# iterate through the pixels, and apply the grayscale transform
    for i in range(len(image)):
        for j in range(len(image[i])):
            gray_val = sum([p * w for p, w in zip(image[i, j], COLOR_WEIGHTS)])
            for c in range(len(gray_image[i, j])):
                gray_image[i, j][c] = gray_val"""
    # Return image (make sure it's the right type!)
    gray_image[:, :, 0] = gray_image[:, :, 1] = gray_image[:, :, 2] = (
        image[:, :, 0] * 0.21000 + image[:, :, 1] * 0.72000 + image[:, :, 2] * 0.07000
    )
    return gray_image


def numba_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image)
    # Iterate through the pixels
    # applying the sepia matrix

    ...

    # Return image
    # don't forget to make sure it's the right type!
    return sepia_image


...
