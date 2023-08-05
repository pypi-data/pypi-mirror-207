
from glob import glob
import os
from pathlib import Path
from PIL.Image import Image, open, fromarray
import numpy as np


DEFAULT_PATH = Path('..', '..', 'data')
VALID_FILE_TYPES = ["jpg", "jpeg", "png"]


def image_name(img):
    return Path(img.filename).name


def empty_image(img):
    return fromarray(np.full(img.size[::-1], 0))


class Dataset():
    def __init__(self, data_path=DEFAULT_PATH):
        self.images_path = data_path / 'images'
        self.labels_path = data_path / 'labels'

        _images = [glob(f'{self.images_path}/*.{ext}') for ext in VALID_FILE_TYPES]
        self.images = [open(item) for i in _images for item in i]

    def get(self, index: int) -> tuple[Image, str]:
        index %= len(self.images)
        image = self.images[index]
        return image, image_name(image)

    def get_labels_for(self, image):
        try:
            return open(f'{self.labels_path}/{image_name(image)}')
        except IOError:
            return empty_image(image)

    def save_labels(self, index: int, data):
        im = fromarray(data.astype(np.uint8))
        _, name = self.get(index)
        save_path = f'{self.labels_path}/{name}'

        if np.sum(im) > 0:
            im.save(save_path)
        elif os.path.exists(save_path):
            os.remove(save_path)
