"""pure Python implementation of image filters"""

import numpy as np

PIXEL_WEIGHTS = np.asarray([0.2100, 0.7200, 0.0700])


def python_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty_like(image)
    # iterate through the pixels, and apply the grayscale transform
    for i in range(len(image)):
        for j in range(len(image[i])):
            gray_val = sum([p * w for p, w in zip(image[i, j], PIXEL_WEIGHTS)])
            for c in range(len(gray_image[i, j])):
                gray_image[i, j][c] = gray_val

    return gray_image


def python_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image, dtype=np.uint8)
    # Iterate through the pixels
    # applying the sepia matrix
    sepia_matrix = np.asarray(
        [
            [0.393, 0.769, 0.189],
            [0.349, 0.686, 0.168],
            [0.272, 0.534, 0.131],
        ],
        dtype="double",
    )

    for i in range(len(image)):
        for j in range(len(image[i])):
            for n in range(3):
                sepia_image[i, j, n] = min(255, sum([p * s for p, s in zip(sepia_matrix[n], image[i, j])]))

    # Return image
    # don't forget to make sure it's the right type!
    return sepia_image
