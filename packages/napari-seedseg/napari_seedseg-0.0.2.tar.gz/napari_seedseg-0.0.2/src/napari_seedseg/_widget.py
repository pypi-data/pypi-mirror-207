from typing import TYPE_CHECKING, Optional, Tuple

import warnings

import numpy as np
from napari.layers import Image
from magicgui.widgets import Container, create_widget, PushButton

from ._layers import SegmentedLayer, ContourLayer
from ._method import Method


if TYPE_CHECKING:
    import napari


class SeedSegWidget(Container):
    """
    A widget for handling Seed Segmentation operations in the napari viewer.

    Attributes
    ----------
    napari_viewer : napari.Viewer
        The napari viewer instance.

    Methods
    -------
    on_confirm() -> None
        Triggered when the 'Confirm' button is clicked.
    create_segmented_layer() -> SegmentedLayer
        Creates and adds an empty segmented layer to the viewer.
        Also, mouse actions are added to callbacks of the segmented layer.
    create_contour_layer() -> ContourLayer
        Creates and adds an empty contour layer to the viewer.
    mouse_move_action(segmented_layer: SegmentedLayer, event) -> None
        Triggered when the mouse moves over the segmented layer.
    mouse_double_click_action(segmented_layer: SegmentedLayer, event) -> None
        Triggered when the mouse double-clicks inside the contour layer. 
        Updates the segmentation mask based on calculated mask by the method.
    on_contour_update(event=None) -> None
        Updates the contour layer data.
    update_tolerance(value: int) -> None
        Updates the tolerance value of the segmentation method.
    validate_confirm() -> bool
        Validates if the 'Confirm' button can be enabled.
    """

    def __init__(self, napari_viewer):
        super().__init__()
        
        self._viewer = napari_viewer
        self._method: Optional[Method] = None

        self._image_layer = create_widget(annotation=Image, label='Image')

        self._tolerance = create_widget(
            10, widget_type='IntSlider', label='Tolerance',
            options=dict(min=1, max=50,
                tooltip='A comparison will be done at every point and if within tolerance of the initial value will also be filled '
            )
        )

        self._tolerance.changed.connect(self.update_tolerance)
                
        self._confirm_button = PushButton(text='Confirm', enabled=False)
        self._confirm_button.changed.connect(self.on_confirm)
        set_button_status = lambda _: setattr(self._confirm_button, 'enabled', self.validate_confirm())
        self._image_layer.changed.connect(set_button_status)

        self.extend([self._image_layer, self._tolerance, self._confirm_button])
        
    def on_confirm(self) -> None:
        """
        Triggered when the 'Confirm' button is clicked. Initializes the segmentation method and layers.
        """

        _image = self._image_layer.value.data
        self._h, self._w = _image.shape

        self._contour_layer = self.create_contour_layer() 
        self._segmented_layer = self.create_segmented_layer()

        self._method = Method(
            _image, _tolerance = self._tolerance.value
        )

        self._viewer.layers.selection = [self._segmented_layer]





    def create_segmented_layer(self)  -> SegmentedLayer:
        """
        Creates and adds an empty segmented layer to the viewer.
        Also, mouse actions are added to callbacks of the segmented layer.

        Returns
        -------
        SegmentedLayer
            The created and added segmented layer.
        """

        _segmented_layer = SegmentedLayer(
            name='Segmented Layer',
            data=np.zeros((self._h, self._w),dtype=int),
            color={1: 'yellow'},
            opacity=0.7
        )

        _segmented_layer.mouse_move_callbacks.append(self.mouse_move_action)
        _segmented_layer.mouse_double_click_callbacks.append(self.mouse_double_click_action)
        _segmented_layer.events.contour_layer.connect(self.on_contour_update)

        return self._viewer.add_layer(_segmented_layer)
    
    def create_contour_layer(self) -> SegmentedLayer:
        """
        Creates and adds an empty contour layer to the viewer.

        Returns
        -------
        ContourLayer
            The created and added contour layer.
        """

        return self._viewer.add_layer(
            ContourLayer(
                name='Contour',
                data=np.zeros((self._h, self._w),dtype=int),
                color={1: 'cyan'},
                opacity=1.0)
            )
    

    def mouse_move_action(self, segmented_layer: SegmentedLayer, event) -> None:
        """
        Triggered when the mouse moves over the segmented layer. Updates the contour based on mouse position.

        Parameters
        ----------
        segmented_layer : SegmentedLayer
            The segmented layer.
        event : Event
            The mouse move event.
        """
        
        if self._method is None:
            return

        # Cast, clip, and round position of the mouse.
        rounded_array = tuple(map(int, np.clip(np.round(event.position), 0, [self._h-1, self._w-1]).astype(int)))

        self._method.compute(rounded_array)
        self.on_contour_update()

    def mouse_double_click_action(self, segmented_layer: SegmentedLayer, event) -> None:
        """
        Triggered when the mouse double-clicks inside the contour layer. 
        Updates the segmentation mask based on calculated mask by the method.

        Parameters
        ----------
        segmented_layer : SegmentedLayer
            The segmented layer.
        event : Event
            The mouse double-click event.
        """
        
        if self._method is None:
            return
        
        self._segmented_layer.update_data(self._method._mask)

    def on_contour_update(self, event=None) -> None:
        """
        Updates the contour layer data.

        Parameters
        ----------
        event : Event, optional, default: None
            The event triggering the update.
        """

        self._contour_layer.update_data(self._method._contour)
    
    def update_tolerance(self, value: int) -> None:
        """
        Updates the tolerance value of the segmentation method.

        Parameters
        ----------
        value : float
            The new tolerance value.
        """

        if self._method is None:
            return
        
        self._method.update_tolerance(value)

    def validate_confirm(self) -> bool:
        """
        Validates if the 'Confirm' button can be enabled.

        Returns
        -------
        bool
            True if the image is 2-dimensional, otherwise False.
        """

        _image = np.array(self._image_layer.value.data)

        if len(_image.shape) != 2:
            warnings.warn(f'`Image` must be 2-dimensional.')
            return False
        
        return True
    
    # For testing stage.
    def _on_click(self):
        print("napari has run")

        
