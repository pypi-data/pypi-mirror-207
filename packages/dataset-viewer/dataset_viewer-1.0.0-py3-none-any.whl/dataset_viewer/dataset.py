
from glob import glob
import os
from pathlib import Path
from PIL.Image import Image, open, fromarray
import numpy as np


DEFAULT_PATH = Path('..', '..', 'data')
VALID_FILE_TYPES = ["jpg", "jpeg", "png"]


def image_name(img):
    '''Gets the image name without extension'''
    return Path(img.filename).name


def image_stem(img):
    '''Gets the image name without extension'''
    return Path(img.filename).stem


def empty_image(img):
    '''Gets an empty image'''
    return fromarray(np.full(img.size[::-1], 0))


class Dataset():
    '''
    A class used to represent a Dataset to show in the Viewer

    Attributes
    ----------
    images : list
        List of all loaded images

    Raises
    -------
    Exception
        If no images can be found
    '''

    def __init__(self, data_path: Path = None):
        '''
        Parameters
        ----------
        data_path : Path
            The path for images and labels
        '''

        if data_path is None:
            data_path = DEFAULT_PATH

        self.images_path = data_path / 'images'
        self.labels_path = data_path / 'labels'

        _images = [glob(f'{self.images_path}/*.{ext}') for ext in VALID_FILE_TYPES]
        self.images = [open(item) for i in _images for item in i]

        if len(self.images) == 0:
            raise Exception('No images were found')


    def get(self, index: int) -> tuple[Image, str]:
        '''Gets a image by index

        Parameters
        ----------
        index: int
            The index of the image

        Returns
        -------
        Image
            The image at the index
        str
            The name of the image
        '''
        index %= len(self.images)
        image = self.images[index]
        return image, image_name(image)

    def get_labels_for(self, image):
        '''Gets the labels image for a specified image

        Parameters
        ----------
        img: Image
            The image to get the labels from

        Returns
        -------
        Image
            the labels image, or an empty image if no labels exists
        '''
        try:
            # We need to save as png since other formats are using compression
            return open(f'{self.labels_path}/{image_stem(image)}.png')
        except IOError:
            return empty_image(image)

    def save_labels(self, index: int, data):
        '''Save the labels for the image

        Parameters
        ----------
        index: int
            Index of the image to save the labels for
        data: Any
            the numpy array containing the labels data
        '''
        im = fromarray(data.astype(np.uint8))
        image, _ = self.get(index)
        save_path = f'{self.labels_path}/{image_stem(image)}.png'

        if np.sum(im) > 0:
            im.save(save_path)
        elif os.path.exists(save_path):
            os.remove(save_path)
