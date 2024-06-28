import numpy as np

from SimExporter.core import Exporter

# Load the simulation data
data = np.load('data.npz')

# Create the exporter
exporter = Exporter(animation=True, fps=25)

# Add objects to the scene
exporter.objects.add_mesh(positions=data['surface_positions'][0],
                          cells=data['surface_triangles'],
                          color='orange',
                          alpha=0.8,
                          time_positions=data['surface_positions'])

# Export to HTML
exporter.process(filename='scene.html',
                 grid_visible=False)
