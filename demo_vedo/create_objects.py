"""
First tutorial to learn Vedo basics:
- create and customize 3d objects (Mesh, TetMesh, Points, Arrows)
- create and display the Plotter, discover functionalities
"""

import numpy as np
import vedo


# Load the simulation data
data = np.load('data.npz')
for key, value in data.items():
    print(key, value.shape)

# Create the plotter
...

# Create a surface mesh and add to the plotter
...

# Create a tetra mesh and add to the plotter
...

# Create a point cloud and add to the plotter
...

# Create vectors and add to the plotter
...

# Display
...
