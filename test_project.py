from project import to_images, get_frames, set_duration
import pytest
from PIL import Image


def test_to_images():
    names = ["blank.png", "cs50.png"]
    images = to_images(names)

    assert (type(images) == list)
    assert (isinstance(images[0], Image.Image))
    assert (len(images) == len(names))


def test_get_frames():
    names = ["blank.png", "cs50.png"]
    images = to_images(names)
    frames = get_frames(*images)

    assert(type(frames) == tuple)
    assert(isinstance(frames[0], Image.Image))
    assert(len(frames) == (len(names) - 1) * 60 + 1)

    names = ["blank.png", "cs50.png"]
    images = to_images(names)
    frames = get_frames(*images, fr = 10)

    assert(type(frames) == tuple)
    assert(isinstance(frames[0], Image.Image))
    assert(len(frames) == (len(names) - 1) * 10 + 1)


def test_set_duration():
    duration = set_duration(181)

    assert(duration[0] == 750)
    assert(duration[34] == 20)
    assert(duration[60] == 750)
    assert(duration[180] == 750)

    duration = set_duration(181, 10)

    assert(duration[0] == 750)
    assert(duration[34] == 20)
    assert(duration[10] == 750)
    assert(duration[180] == 750)
