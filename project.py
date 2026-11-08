"""
A tool that we pass a few images and it will create a transition gif out of it!
"""

import sys
from PIL import Image, ImageOps
from animator import Animator
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs = "+", type = str, help="Input atleast two image file names.")
    parser.add_argument("-o", type = str, default="animation.gif", help="Name the output GIF file.")
    args = parser.parse_args()

    images = to_images(args.images)

    # better to keep size around 200 for quick creation of your gif :)
    frames = get_frames(*images, fr = 60, size = 200)

    generate_gif(frames, args.o)


def to_images(names):
    """
    Creates Image objects from given filenames and returns them in a list.
    """
    return [Image.open(n) for n in names]


def get_frames(*images, fr = 60, size = 200):
    """
    Generates transition frames between the given images and returns them in a tuple.
    """

    animator = Animator(*images, fr = fr, size = size)
    return animator.generate()


def generate_gif(frames, name, fr = 60):
    """
    Generates a .gif file in the current folder using the given list of images
    """
    durations = set_duration(len(frames), fr)

    if frames:
        frames[0].save(
            name,
            save_all = True,
            append_images = frames[1:],
            duration = durations,
            loop = 0,
            optimize = False
        )
        print("GIF created successfully!")
    else:
        print("Enter atleast two images.")



def set_duration(n, fr = 60):
    """
    Generates a list of numbers representing duration in milliseconds of each frame in the gif.
    It gives a frame at equal intervals more duration of 750ms, and 20ms for the rest of frames.
    """
    return [750 if i % fr == 0 else 20 for i in range(n)]


if __name__ == "__main__":
    main()


