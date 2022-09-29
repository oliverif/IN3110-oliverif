
import numpy as np
cimport numpy as np


def cython_color2gray(image):
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    #cdef np.ndarray[np.float_t,ndim=1] PIXEL_WEIGHTS = np.asarray([0.21, 0.72, 0.07])

    #cdef np.ndarray[np.uint8_t,ndim=3] img = image
    cdef np.ndarray[np.uint8_t,ndim=3] gray_image = np.empty_like(image)
    #cdef np.ndarray[np.double_t,ndim=3] res = img * PIXEL_WEIGHTS
    #gray_image[:, :,:] = np.sum(res, axis=2, keepdims=True)

    #gray_image = np.empty_like(image)
    # Return image (make sure it's the right type!)
    cdef double r = 0.21
    cdef double g = 0.71
    cdef double b = 0.07
    cdef int first = 0
    cdef int second = 1
    cdef int third = 2
    gray_image[:, :, first] = gray_image[:, :, second] = gray_image[:, :, third] = (
        image[:, :, first] * r + image[:, :, second] * g + image[:, :, third] * b
    )
    return gray_image

def cython_color2sepia(image):
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    ...
