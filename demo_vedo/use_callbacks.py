import numpy as np
import vedo

# Load the simulation data
data = np.load('data.npz')

# Create the plotter
...

# Create the surface mesh, apply a colormap and add to the plotter
...


def key_callback(event):
    """
    External function to be called by the key pressed event.
    """

    # Check the key pressed value and update the background color
    ...


def time_callback(event):
    """
    External function to be called by the timer.
    """

    # Update the current step
    ...


# Add callbacks
...

# Display
...
