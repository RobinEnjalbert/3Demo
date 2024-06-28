import numpy as np
import vedo


# Load the simulation data
data = np.load('data.npz')

# Create the plotter
plt = vedo.Plotter()

# Create a surface mesh
surface_mesh = vedo.Mesh(inputobj=[data['surface_positions'][0], data['surface_triangles']], c='orange5', alpha=0.8)
plt.add(surface_mesh)

# Create a tetra mesh
tetra_mesh = vedo.TetMesh(inputobj=[data['volume_positions'][0], data['volume_tetras']]).color(c='blue7')
plt.add(tetra_mesh.clone().shrink(0.8))

# Create a point cloud
constraint_pcd = vedo.Points(inputobj=data['constraints'], r=10, c='red3')
plt.add(constraint_pcd)

# Create vectors
forces_vectors = [vedo.Arrows(start_pts=tetra_mesh.vertices[data[f'force_idx_{i}']],
                              end_pts=tetra_mesh.vertices[data[f'force_idx_{i}']] + data[f'force_value_{i}'],
                              c='green4', res=10)
                  for i in range(4)]
plt.add(*forces_vectors)

# Display
plt.show()
