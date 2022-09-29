"""
Timing our filter implementations.

Can be executed as `python3 -m instapy.timing`

For Task 6.
"""
import time
from instapy import io, python_filters, numpy_filters, cython_filters
from instapy.numba_filters import *
from typing import Callable
import sys

FILTERS = {
    "pure Python": python_filters.python_color2gray,
    "numpy": numpy_filters.numpy_color2gray,
    "numba": numba_color2gray,
    "cython": cython_filters.cython_color2gray,
}


def time_one(filter_function: Callable, *arguments, calls: int = 3) -> float:
    """Return the time for one call

    When measuring, repeat the call `calls` times,
    and return the average.

    Args:
        filter_function (callable):
            The filter function to time
        *arguments:
            Arguments to pass to filter_function
        calls (int):
            The number of times to call the function,
            for measurement
    Returns:
        time (float):
            The average time (in seconds) to run filter_function(*arguments)
    """
    # By running the function once before timing, the Numba implementation improved significantly. This is likely because
    # the compiling of the function is happening outside the loop, so that the timer is not including this. Compiling
    # outside allows for caching of the compiled script for reuse in loops.
    result = filter_function(*arguments)

    # run the filter function `calls` times
    tot_time = 0
    for i in range(calls):
        then = time.time()
        result = filter_function(*arguments)
        now = time.time()
        tot_time += now - then

    # return the _average_ time of one call
    return tot_time / calls


def make_reports(filename: str = "test/rain.jpg", calls: int = 3):
    """
    Make timing reports for all implementations and filters,
    run for a given image.

    Args:
        filename (str): the image file to use
    """

    # load the image
    image = io.read_image(filename)
    # print the image name, width, height
    print(f"Timing performed using {filename}: {image.shape[1]}x{image.shape[0]}\n")
    # iterate through the filters
    filter_names = ["color2gray", "color2sepia"]
    for filter_name in filter_names:
        # get the reference filter function
        reference_filter = FILTERS["pure Python"]
        # time the reference implementation
        reference_time = time_one(reference_filter, image, calls=3)
        print(f"Reference (pure Python) filter time {filter_name}: {reference_time:.3}s ({calls=})")
        # iterate through the implementations
        implementations = ["numpy", "numba", "cython"]
        for implementation in implementations:
            filter = FILTERS[implementation]
            # time the filter
            filter_time = time_one(filter, image, calls=3)
            # compare the reference time to the optimized time
            speedup = reference_time / filter_time
            print(f"Timing: {implementation} {filter_name}: {filter_time:.3}s ({speedup=:.2f}x)")
        print("\n")


if __name__ == "__main__":
    # run as `python -m instapy.timing`
    with open("timing-report.txt", "w") as f:
        sys.stdout = f
        make_reports(calls=3)
