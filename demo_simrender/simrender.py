import numpy as np

from SimRender.core import Viewer


class Simulation:

    def __init__(self, view: Viewer):

        self.viewer = view
        self.data = np.load('data.npz')
        self.id_step = 0
        self.nb_step = self.data['surface_positions'].shape[0]

    def init_viewer(self):

        # Add triangle surface mesh
        self.viewer.objects.add_mesh(positions=self.data['surface_positions'][0],
                                     cells=self.data['surface_triangles'],
                                     color='orange5', alpha=0.8, line_width=0)

        # Add tetra volume mesh
        self.viewer.objects.add_mesh(positions=self.data['volume_positions'][0],
                                     cells=self.data['volume_tetras'],
                                     color='blue7', wireframe=False, alpha=0.6)

        # Add constraints points
        self.viewer.objects.add_points(positions=self.data['constraints'],
                                       color='red3', alpha=0.9, point_size=15)

        # Add forces arrows
        pos = np.concatenate([self.data['volume_positions'][0][self.data[f'force_idx_{i}']] for i in range(4)])
        vec = np.concatenate([self.data[f'force_value_{i}'] for i in range(4)])
        self.viewer.objects.add_arrows(positions=pos,
                                       vectors=vec,
                                       color='green')

    def step(self):

        # Update time step
        self.id_step = (self.id_step + 10) % self.nb_step

        # Update surface mesh
        self.viewer.objects.update_mesh(object_id=0,
                                        positions=self.data['surface_positions'][self.id_step])

        # Update volume mesh
        self.viewer.objects.update_mesh(object_id=1,
                                        positions=self.data['volume_positions'][self.id_step])

        # Update forces
        pos = np.concatenate([self.data['volume_positions'][self.id_step][self.data[f'force_idx_{i}']] for i in range(4)])
        self.viewer.objects.update_arrows(object_id=3, positions=pos)


if __name__ == '__main__':

    # Create the simulation and the viewer
    viewer = Viewer()
    simu = Simulation(view=viewer)

    # Init the visualization
    simu.init_viewer()
    viewer.launch()

    # Run some steps of the simulation
    for _ in range(simu.nb_step):
        simu.step()
        viewer.render()

    # Close the rendering window
    viewer.shutdown()
