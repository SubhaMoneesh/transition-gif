import numpy as np
from PIL import Image, ImageOps


class Animator:
    def __init__(self, *images, fr = 30, size = 200):
        self.fr = fr
        self.size = size
        self.images = images


    @property
    def images(self) -> tuple:
        return self._images


    @images.setter
    def images(self, new_images):
        sized_imgs = []
        for i in new_images:
            sized_imgs.append(ImageOps.contain(i, (self.size, self.size)).convert("1"))

        self._images = tuple(sized_imgs)


    def generate(self) -> tuple:
        result = []

        for image1, image2 in zip(self.images, self.images[1:]):
            frames = self.animate(image1, image2)

            result.extend(frames if not result else frames[1:])


        return tuple(result)


    def animate(self, image1, image2) -> tuple:
        arr1 = np.array(image1)
        arr2 = np.array(image2)

        blacks1 = self.get_blacks_path(arr1, arr2)
        blacks2 = self.get_blacks_path(arr2, arr1)

        frames1 = self.create_frames(blacks1)
        frames2 = self.create_frames(blacks2)

        final_frames = self.join_frames(frames1, frames2)

        final_images: list = self.convert_to_images(final_frames)

        return final_images


    def convert_to_images(self, frames):
        final_images = [Image.fromarray(frame) for frame in frames]

        return final_images


    def join_frames(self, frames1, frames2):
        frames = [frame & frames2[self.fr - i] for i, frame in enumerate(frames1)]

        return frames


    def create_frames(self, blacks):
        blacks_arr = np.array(blacks).reshape(-1, 4)

        start = blacks_arr[:, :2]
        end = blacks_arr[:, 2:]

        movement = (end - start) / self.fr

        frames = []

        for i in range(self.fr + 1):
            frame = np.full((self.size, self.size), True, dtype=bool)

            positions = (start + i * movement).astype(int)

            frame[positions[:, 0], positions[:, 1]] = False

            frames.append(frame)

        return frames


    def get_blacks_path(self, arr1, arr2):
        blacks1 = []

        indices1 = np.argwhere(~arr1)
        indices2 = np.argwhere(~arr2)

        for i, j in indices1:
            min_dist = 2 * self.size
            target = (0, 0)

            for k, l in indices2:
                dist = abs(i - k) + abs(j - l)
                if min_dist > dist:
                    min_dist = dist
                    target = (k, l)

            blacks1.append([i, j, *target])


        return blacks1
