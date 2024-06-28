import numpy as np
import vedo


# Load the simulation data
data = np.load('data.npz')

# Create the plotter
plt = vedo.Plotter()

# Create the surface mesh
surface_mesh = vedo.Mesh(inputobj=[data['surface_positions'][0], data['surface_triangles']])
surface_mesh_disp = surface_mesh.clone().cmap(input_cmap='jet', input_array=np.zeros_like(surface_mesh.vertices),
                                              vmin=0, vmax=3.5)
plt.add(surface_mesh.color(c='orange5', alpha=0.8))


def slider_fnc(widget, event):

    # Update the surface meshes
    surface_mesh.vertices = data['surface_positions'][int(widget.value)]
    surface_mesh_disp.vertices = data['surface_positions'][int(widget.value)]
    disp = np.linalg.norm(surface_mesh.vertices - data['surface_positions'][0], axis=1)
    surface_mesh_disp.cmap(input_cmap='jet', input_array=disp, vmin=0, vmax=3.5)

    # Update the plotter
    plt.render()


def button_fnc(widget, event):

    # Display the displacement field
    if 'Show' in widget.status():
        plt.remove(surface_mesh)
        plt.add(surface_mesh_disp)

    # Display the default color
    else:
        plt.remove(surface_mesh_disp)
        plt.add(surface_mesh)

    # Update the plotter
    widget.switch()
    plt.render()


# Add widgets
plt.add_slider(sliderfunc=slider_fnc, title='time', xmin=0, xmax=500)
plt.add_button(fnc=button_fnc, states=['Show displacement field', 'Hide displacement field'],
               pos=[0.25, 0.075], size=20)

# Display
plt.show()
