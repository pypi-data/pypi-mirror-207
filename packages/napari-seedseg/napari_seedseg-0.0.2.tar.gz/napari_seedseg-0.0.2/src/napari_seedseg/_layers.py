import numpy as np

from napari.layers.labels import Labels 
from napari.utils.events import Event


class ContourLayer(Labels):
    """
    A custom ContourLayer class that inherits from napari's Labels layer.

    Methods
    -------
    update_data(data: np.ndarray) -> None
        Updates the layer's data.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def update_data(self, data: np.ndarray) -> None:
        """
        Updates the layer's data.

        Parameters
        ----------
        data : np.ndarray
            The new data to update the layer with.
        """

        self.data = data
        

class SegmentedLayer(Labels):
    """
    A custom SegmentedLayer class that inherits from napari's Labels layer.

    Methods
    -------
    update_data(data: np.ndarray) -> None
        Updates the layer's data.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.events.add(
            contour_layer=Event,
        )
    
    def update_data(self, data: np.ndarray) -> None:
        """
        Updates the layer's data.

        Parameters
        ----------
        data : np.ndarray
            The new data to update the layer with.
        """

        self.data = np.clip (self.data + data, 0, 1).astype(int)
                