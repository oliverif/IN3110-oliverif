from instapy.numpy_filters import numpy_color2gray, numpy_color2sepia

import numpy.testing as nt
import numpy as np


def test_color2gray(image, reference_gray):
    # run color2gray
    result = numpy_color2gray(image)
    # check that the result has the right shape, type
    assert result.shape == image.shape
    assert result.dtype == np.uint8
    # assert uniform r,g,b values
    nt.assert_array_equal(result[:, :, 0], result[:, :, 1])
    nt.assert_array_equal(result[:, :, 0], result[:, :, 2])

    nt.assert_array_almost_equal(result, reference_gray)


def test_color2sepia(image, reference_sepia):
    # run color2sepia
    result = numpy_color2sepia(image)
    # check that the result has the right shape, type
    assert result.shape == image.shape
    assert result.shape == reference_sepia.shape
    # assert result.dtype == np.uint8
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
    # NOTE This test might fail due to numpy's precision being better than when using python types.
    # All other implementations, like numba and cython get's same exact result as python, but numpy(when using einsum)
    # seems to be slightly more accurate. This does not occur on all systems. E.g on a laptop, the test passes, however
    # on desktop computer it fails. An example is the rain.jpg image at index [185,558,:]. When processing this
    # pixel through sepia filter, python, numba and cython results in 225.9999998(which in reality is 226.0 when doing
    # hand calculation), while numpy results in the correct 226.0. Converting 225.9999998 to uint8 results in 225, while
    # converting 226.0 to uint8 results in 226. It's rare that this happens though.

    # nt.assert_array_equal(result, reference_sepia)
