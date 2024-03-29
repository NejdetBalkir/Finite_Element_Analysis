import numpy as np
from ShapeFunction import shapeFuncQ4
from Jacobian import Jacobian
def CalculateStress(nE,nP,elNode,disp,xy,C):

    # Objective:
    # ------------This function calculates and average stresses at nodes
    # Inputs:
    # ------------nE: Number of elements
    # ------------nP: Number of nodes
    # ------------elNode: Element connectivity
    # ------------disp: Displacement vector
    # ------------xy: Nodal coordinates
    # ------------C: Constitutive matrix

    # Outputs:
    # ------------stress: Average stress at nodes

    # Initialization arrays for element-level stress and strain

    Sxx_FEM = np.zeros((nE, 4))
    Syy_FEM = np.zeros((nE, 4))
    Sxy_FEM = np.zeros((nE, 4))

    exx_FEM = np.zeros((nE, 4))
    eyy_FEM = np.zeros((nE, 4))
    exy_FEM = np.zeros((nE, 4))

    # Initialization arrays for nodal-level stress and strain
    Sxx_node_FEM = np.zeros((nP, 1))
    Syy_node_FEM = np.zeros((nP, 1))
    Sxy_node_FEM = np.zeros((nP, 1))

    exx_node_FEM = np.zeros((nP, 1))
    eyy_node_FEM = np.zeros((nP, 1))
    exy_node_FEM = np.zeros((nP, 1))

    # Natural coordinates
    natural_Coord = np.array([[-1, -1], [1, -1], [1, 1], [-1, 1]])

    # Loop over elements
    for ie in range(nE):
        id = elNode[ie, :]
        elDof = np.concatenate([id,id +nP])

        # Loop over Gauss points(natural coordinates)
        for j,(xi_norm,eta_norm) in enumerate(natural_Coord):

            shape_norm , nDeriva_norm = shapeFuncQ4(xi_norm,eta_norm)
            J_norm , xyDeriva_norm = Jacobian(xy[id,:],nDeriva_norm)

            B_norm = np.zeros((3, 8)) # Strain-displacement matrix
            ndof = len(id)
            B_norm[0, 0:ndof] = xyDeriva_norm[:, 0]
            B_norm[1, ndof:2*ndof] = xyDeriva_norm[:, 1]
            B_norm[2, 0:ndof] = xyDeriva_norm[:, 1]
            B_norm[2, ndof:2*ndof] = xyDeriva_norm[:, 0]

            # Displacement vector
            Uei = disp[elDof]
            ei_norm = B_norm @ Uei
            Si_norm = C @ ei_norm

            # Store element-level stress and strain
            exx_FEM[ie, j] = ei_norm[0]
            eyy_FEM[ie, j] = ei_norm[1]
            exy_FEM[ie, j] = ei_norm[2]
            Sxx_FEM[ie, j] = Si_norm[0]
            Syy_FEM[ie, j] = Si_norm[1]
            Sxy_FEM[ie, j] = Si_norm[2]
    
    # Average stress and strain at nodes
    for i in range(nP):
        for j in range(4):
            idi = np.where(elNode[:,j] == i)[0]
            ni = len(idi)
            if ni > 0:
                Sxx_node_FEM[i] += np.sum(Sxx_FEM[idi,j])
                Syy_node_FEM[i] += np.sum(Syy_FEM[idi,j])
                Sxy_node_FEM[i] += np.sum(Sxy_FEM[idi,j])
                exx_node_FEM[i] += np.sum(exx_FEM[idi,j])
                eyy_node_FEM[i] += np.sum(eyy_FEM[idi,j])

        if ni > 0:
            Sxx_node_FEM[i] /= ni
            Syy_node_FEM[i] /= ni
            exx_node_FEM[i] /= ni
            eyy_node_FEM[i] /= ni

    return Sxx_node_FEM, Syy_node_FEM, Sxy_node_FEM


