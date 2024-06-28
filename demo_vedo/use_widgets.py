import numpy as np
import vedo


# Load the simulation data
data = np.load('data.npz')

# Create the plotter
...

# Create the surface mesh, apply a colormap and add to the plotter
...


def slider_fnc(widget, event):
    """
    External function to be called by the slider widget.
    """

    # Update the surface meshes
    ...

    # Update the plotter
    ...


def button_fnc(widget, event):
    """
    External function to be called by the button.
    """

    # Display / Hide the displacement field
    ...

    # Update the plotter
    ...


# Add widgets
...

# Display
...
