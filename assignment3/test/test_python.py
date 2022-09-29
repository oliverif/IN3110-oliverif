from instapy.python_filters import python_color2gray, python_color2sepia
import numpy as np
import pytest


def test_color2gray(image):
    # run color2gray
    result = python_color2gray(image)
    # check that the result has the right shape, type
    assert result.shape == image.shape
    assert result.dtype == np.uint8
    # assert uniform r,g,b values
    np.testing.assert_array_equal(result[:, :, 0], result[:, :, 1])
    np.testing.assert_array_equal(result[:, :, 0], result[:, :, 2])


def test_color2sepia(image):
    # run color2sepia
    result = python_color2sepia(image)
    # check that the result has the right shape, type
    assert result.shape == image.shape
    assert result.dtype == np.uint8
    # verify some individual pixel samples
    # according to the sepia matrix
    assert result[0, 0, 0] == int(min(image[0, 0, 0] * 0.393 + image[0, 0, 1] * 0.769 + image[0, 0, 2] * 0.189, 255))
    assert result[0, 0, 1] == int(min(image[0, 0, 0] * 0.349 + image[0, 0, 1] * 0.686 + image[0, 0, 2] * 0.168, 255))
    assert result[0, 0, 2] == int(min(image[0, 0, 0] * 0.272 + image[0, 0, 1] * 0.534 + image[0, 0, 2] * 0.131, 255))

    assert result[5, 56, 0] == int(
        min(image[5, 56, 0] * 0.393 + image[5, 56, 1] * 0.769 + image[5, 56, 2] * 0.189, 255)
    )
    assert result[5, 56, 1] == int(
        min(image[5, 56, 0] * 0.349 + image[5, 56, 1] * 0.686 + image[5, 56, 2] * 0.168, 255)
    )
    assert result[5, 56, 2] == int(
        min(image[5, 56, 0] * 0.272 + image[5, 56, 1] * 0.534 + image[5, 56, 2] * 0.131, 255)
    )
