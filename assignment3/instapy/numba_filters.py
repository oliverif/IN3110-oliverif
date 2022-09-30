"""numba-optimized filters"""
from numba import jit
import numpy as np


@jit(nopython=True, cache=True)
def numba_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    gray_image = np.empty_like(image)

    # These predefenitions will allow numba to convert more of the code to c code.
    nx = image.shape[1]
    ny = image.shape[0]
    r = 0.2100
    g = 0.7200
    b = 0.0700

    # Iterate through image and assign gray value to numpy array
    for i in range(ny):
        for j in range(nx):
            gray_val = image[i, j, 0] * r + image[i, j, 1] * g + image[i, j, 2] * b  # Cast result to uint8
            gray_image[i, j, 0] = gray_image[i, j, 1] = gray_image[i, j, 2] = gray_val  # Faster than gray_image[i,j,:]
    return gray_image.astype(np.uint8)


@jit(nopython=True, cache=True)
def numba_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image, dtype="uint8")
    # Iterate through the pixels
    # applying the sepia matrix

    sepia_matrix = np.asarray(
        [
            [0.393, 0.769, 0.189],
            [0.349, 0.686, 0.168],
            [0.272, 0.534, 0.131],
        ]
    )
    nx = image.shape[1]
    ny = image.shape[0]

    for i in range(ny):
        for j in range(nx):
            for n in range(3):
                tmp = 0
                for m in range(3):
                    tmp += sepia_matrix[n, m] * image[i, j, m]

                sepia_image[i, j, n] = min(tmp, 255)
                # sepia_image[i, j, n] = min(255, sum([p * s for p, s in zip(sepia_matrix[n], image[i, j])]))

    # Return image
    # don't forget to make sure it's the right type!
    return sepia_image


...
