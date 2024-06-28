import numpy as np
import vedo

# Load the simulation data
data = np.load('data.npz')
step_id = 0

# Create the plotter
backgrounds = ['white', 'black', 'red', 'blue']
background_id = 0
plt = vedo.Plotter(bg=backgrounds[0])

# Create the surface mesh
surface_mesh = vedo.Mesh(inputobj=[data['surface_positions'][0], data['surface_triangles']])
surface_mesh_disp = surface_mesh.clone().cmap(input_cmap='jet', input_array=np.zeros_like(surface_mesh.vertices),
                                              vmin=0, vmax=3.5)
plt.add(surface_mesh.color(c='orange5', alpha=0.8))


def key_callback(event):
    global background_id
    if event.keypress == 'b':
        background_id = (background_id + 1) % len(backgrounds)
        plt.background(c1=backgrounds[background_id])
        plt.render()


def time_callback(event):
    global step_id
    step_id = (step_id + 5) % len(data['surface_positions'])
    surface_mesh.vertices = data['surface_positions'][step_id]
    plt.render()


# Add callbacks
plt.add_callback(event_name='keypress', func=key_callback)
plt.add_callback(event_name='timer', func=time_callback)
plt.timer_callback(action='create', dt=1)

# Display
plt.show()
