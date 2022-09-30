from pathlib import Path
from functools import lru_cache

import pytest

from instapy import io
from instapy.python_filters import python_color2gray, python_color2sepia
from instapy.numpy_filters import numpy_color2gray, numpy_color2sepia
import numpy as np

test_dir = Path(__file__).absolute().parent


@lru_cache()
def default_image():
    return io.read_image(test_dir.joinpath("rain.jpg"))


@lru_cache()
def random_image():
    # use seed to always generate the same image
    # useful for debugging
    np.random.seed(1)
    return io.random_image()


@pytest.fixture
def image():
    """Fixture to return an image to test with"""
    # return random_image().copy()
    return default_image().copy()


@pytest.fixture
@lru_cache()
def reference_gray():
    """Fixture for a reference color2gray image

    To compare with optimized implementations
    """
    return python_color2gray(default_image())


@pytest.fixture
@lru_cache()
def reference_sepia():
    """Fixture for a reference color2sepia image

    To compare with optimized implementations
    """
    return python_color2sepia(default_image())


@pytest.fixture
def sepia_matrix():
    return np.asarray(
        [
            [0.393, 0.769, 0.189],
            [0.349, 0.686, 0.168],
            [0.272, 0.534, 0.131],
        ]
    )
