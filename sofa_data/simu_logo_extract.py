import numpy as np
import Sofa

from simu_logo import Simulation


if __name__ == '__main__':

    root = Sofa.Core.Node('root')
    simu = root.addObject(Simulation(root=root))
    Sofa.Simulation.init(root)

    # Surface
    surface_positions = [root.logo.visual.getObject('ogl').position.array().copy()]
    surface_triangles = root.logo.visual.getObject('ogl').triangles.value

    # Volume
    volume_positions = [root.logo.getObject('state').position.array().copy()]
    volume_tetras = root.logo.getObject('topology').tetrahedra.value

    # Constraints
    constraints = root.logo.getObject('state').position.value[root.logo.getObject('constraints').indices.value]

    # Forces
    forces_indices = {f'force_idx_{i}': root.logo.forces.getObject(f'cff_{i}').indices.value for i in range(4)}
    forces_value = {f'force_value_{i}': np.tile(root.logo.forces.getObject(f'cff_{i}').forces.value,
                                                len(forces_indices[f'force_idx_{i}'])).reshape(-1, 3) for i in range(4)}

    for _ in range(500):

        Sofa.Simulation.animate(root, root.dt.value)

        surface_positions.append(root.logo.visual.getObject('ogl').position.array().copy())
        volume_positions.append(root.logo.getObject('state').position.array().copy())

    np.savez('logo.npz',
             surface_positions=np.array(surface_positions),
             surface_triangles=surface_triangles,
             volume_positions=np.array(volume_positions),
             volume_tetras=volume_tetras,
             constraints=constraints,
             **forces_value,
             **forces_indices)
