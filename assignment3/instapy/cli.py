"""Command-line (script) interface to instapy"""

import argparse
import sys

import numpy as np
from PIL import Image

import instapy
from instapy.timing import time_one
from . import io


def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1,
) -> None:
    """Run the selected filter"""
    # load the image from a file
    image = io.read_image(file)
    if scale != 1:
        # Resize image, if needed
        image = image.resize((image.width // scale, image.height // scale))

    # Apply the filter
    filter_func = instapy.get_filter(filter, implementation)
    filtered = filter_func(image)
    if out_file:
        # save the file
        io.write_image(filtered, out_file)
    else:
        # not asked to save, display it instead
        io.display(filtered)


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(prog="python3 -m instapy", description="Image filter python module.")

    # filename is positional and required
    parser.add_argument("file", help="The filename to apply filter to")
    parser.add_argument("-o", "--out", help="The output filename")

    group = parser.add_mutually_exclusive_group()
    # Add required arguments
    group.add_argument("-g", "--gray", help="Select gray filter", action="store_true")
    group.add_argument("-se", "--sepia", help="Select sepia filter", action="store_true")
    parser.add_argument("-sc", "--scale", help="Scale factor to resize image", type=int, default=1)
    parser.add_argument(
        "-i",
        "--implementation",
        help="The implementation",
        choices=["python", "numba", "numpy", "cython"],
        default="python",
    )
    parser.add_argument("-r", "--runtime", help="Track average runtime", action="store_true")
    # parse arguments and call run_filter
    args = parser.parse_args()

    if args.gray or (not args.gray and not args.sepia):
        filter = "color2gray"
    elif args.sepia:
        filter = "color2sepia"

    if args.runtime:
        runtime = time_one(instapy.get_filter(filter, args.implementation), io.read_image(args.file))
        print(f"Average time over 3 runs: {runtime}s")
    else:
        run_filter(
            file=args.file, out_file=args.out, implementation=args.implementation, filter=filter, scale=args.scale
        )
