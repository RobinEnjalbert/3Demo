import numpy as np

from SimRender.core import Viewer


class Simulation:

    def __init__(self, view: Viewer):

        # Viewer used by the simulation
        self.viewer = view

        # Load pre-computed data
        self.data = np.load('data.npz')

        # Emulate time steps
        self.id_step = 0
        self.nb_step = self.data['surface_positions'].shape[0]

    def init_viewer(self):

        # Add triangle surface mesh
        ...

        # Add tetra volume mesh
        ...

        # Add constraints points
        ...

        # Add forces arrows
        ...

    def step(self):

        # Update time step
        self.id_step = (self.id_step + 10) % self.nb_step

        # Update surface mesh
        ...

        # Update volume mesh
        ...

        # Update forces
        ...


if __name__ == '__main__':

    # Create the simulation and the viewer
    ...

    # Init the visualization
    ...

    # Run some steps of the simulation
    ...

    # Close the rendering window
    ...
