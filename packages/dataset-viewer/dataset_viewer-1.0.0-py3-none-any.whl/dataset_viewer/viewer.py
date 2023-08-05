import napari
from napari import Viewer as NapariViewer, layers
import numpy as np

from dataset_viewer.dataset import Dataset


class Viewer():
    '''
    A class used to represent a Dataset to show in the Viewer

    Attributes
    ----------
    viewer : Viewer
        The viewer gui instance
    dataset : Dataset
        The current viewer dataset

    Methods
    -------
    start()
        Start the viewer gui with the current dataset
    '''

    __image_idx = 0

    def __init__(self, dataset: Dataset = None):
        self.viewer = NapariViewer()
        self.dataset = dataset if dataset is not None else Dataset()

        self.labels_layer = None
        self.__set_bindings()

    def start(self):
        '''Starts the viewer gui with the first image in the dataset'''
        self.__show_image(0)
        napari.run()

    def __set_bindings(self):
        '''Set the current viewer key bindings'''
        # TODO: Add reset option ('r')
        self.__bind_key('l', self.__current_label_name)
        self.__bind_key('Escape', self.__exit)
        self.__bind_key('Left', self.__previous)
        self.__bind_key('Right', self.__next)

    def __bind_key(self, key, func):
        '''Set a key binding the the viewer'''
        self.viewer.bind_key(key, func)

    def __previous(self, viewer: NapariViewer):
        self.__show_image(-1)

    def __next(self, viewer: NapariViewer):
        self.__show_image(1)

    def __show_image(self, move=0):
        '''Save current image labels and goes to the next image

        Parameters
        ----------
        move : int
            movement applied to the current image index.
            0 to show the current image, 1 to show next, -1 to show previous
        '''
        if self.labels_layer is not None:
            self.dataset.save_labels(self.__image_idx, self.labels_layer.data)

        self.__image_idx += move
        self.viewer.layers.clear()

        image, name = self.dataset.get(self.__image_idx)
        self.viewer.add_image(np.array(image), name=name)
        self.__set_labels_layer(image)

    def __set_labels_layer(self, image):
        '''Set the labels layer for an image

        Parameters
        ----------
        image : Image
            Image to set the labels layer from
        '''
        labels = self.dataset.get_labels_for(image)
        self.labels_layer = self.viewer.add_labels(np.array(labels), name='segmentation')
        self.labels_layer.mode = 'PAINT'

    def __current_label_name(self, viewer: NapariViewer):
        active_layer = viewer.layers.selection.active

        if active_layer is not None:
            print(viewer.layers.selection.active.name)

    def __exit(self, viewer: NapariViewer):
        viewer.close()
