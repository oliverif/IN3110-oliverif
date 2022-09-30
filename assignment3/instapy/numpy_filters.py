"""numpy implementation of image filters"""

from typing import Optional
import numpy as np


def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    gray_image = np.empty_like(image)

    # Multiply color weights with image allows vectorized multiplication.
    # Summing along axis 2 and assingning directly to the axis 2 of gray image.
    gray_image[:, :, 0] = gray_image[:, :, 1] = gray_image[:, :, 2] = (
        image[:, :, 0] * 0.21 + image[:, :, 1] * 0.72 + image[:, :, 2] * 0.07
    )
    return gray_image.astype(np.uint8)


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

    sepia_image = np.empty_like(image, dtype=np.uint8)

    # define sepia matrix (optional: with `k` tuning parameter for bonus task 13)
    sepia_matrix = np.add(
        np.asarray(
            [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
            ]
        )
        * (1 - k),
        np.asarray(
            [
                [0.393, 0.769, 0.189],
                [0.349, 0.686, 0.168],
                [0.272, 0.534, 0.131],
            ],
        )
        * k,
    )

    # HINT: For version without adaptive sepia filter, use the same matrix as in the pure python implementation
    # use Einstein sum to apply pixel transform matrix
    # Apply the matrix filter and clip the values to 255. Note that out=sepia_image ensures the type of sepia_image is
    # presevered.
    sepia_image = np.clip(
        np.einsum("ijk,lk->ijl", image, sepia_matrix, optimize=True),
        a_min=0,
        a_max=255,
        out=sepia_image,
        casting="unsafe",
    )
    return sepia_image
