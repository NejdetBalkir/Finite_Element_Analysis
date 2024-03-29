# THIS CODE GENERATES THE STIFFNESS MATRIX FOR A QUADRILATERAL ELEMENT #

import numpy as np
from GaussQuadrature import Gauss_Quadrature
from ShapeFunction import shapeFuncQ4
from Jacobian import Jacobian

def StiffnessMatrix(nDof,nE,elNode,nP,xy,C,dens,h):

    # INPUTS:
    #     nDof: number of degrees of freedom per node
    #     nE: number of elements
    #     elNode: connectivity matrix
    #     nP: number of nodes
    #     xy: nodal coordinates
    #     C: constitutive matrix
    #     dens: density
    #     h: thickness


    # OUTPUTS:
    #     stiff: global stiffness matrix
    #     mass: global mass matrix

    # initialization a stiffness and mass matrix (nDof*nDof)
    stiff = np.zeros((nDof,nDof))
    mass = np.zeros((nDof,nDof))

    # Gauss points and weights
    number_of_Gauss_points_per_direction = 2
    [gauss_points,gauss_weights] = Gauss_Quadrature(number_of_Gauss_points_per_direction)


    # for ele in range(nE): # loop over elements
    #     element_node_id = elNode[ele,:] # extract element nodes
    #     # extract element degree of freedom
    #     ele_dof = np.hstack([element_node_id,element_node_id+nP])
    #     ndof = len(element_node_id) # number of degrees of freedom per element

    #     for iGauss in range(len(gauss_weights)): # loop over Gauss points
    #         gauss_points_local = gauss_points[iGauss,:] # extract local Gauss points
    #         xi = gauss_points_local[0] # Gauss point in x direction
    #         eta = gauss_points_local[1] # Gauss point in y direction
    #         [shape,naturalDerivatives] = shapeFuncQ4(xi,eta) # calculate shape functions and natural derivatives
    #         J,xyDerivatives = Jacobian(xy[element_node_id,:],naturalDerivatives)  # compute Jacobian matrix and natural derivatives
    #         print('J',J)
    #         print('xyDerivatives',xyDerivatives)

    #         # compute B matrix
    #         B = np.zeros((3,2*ndof)) # initialize B matrix

    #         B[0, 0:ndof] = xyDerivatives[:, 0].T
    #         B[1, ndof:(2*ndof)] = xyDerivatives[:, 1].T
    #         B[2, 0:ndof] = xyDerivatives[:, 1].T
    #         B[2, ndof:(2*ndof)] = xyDerivatives[:, 0].T

    #         # compute stiffness matrix
    #         # stiff_contribution=  B.T.dot(C).dot(B).gauss_weights[iGauss]*np.linalg.det(J)*h
    #         # stiff[np.ix_(ele_dof,ele_dof)] += stiff_contribution
    #         # print('stiff',stiff)
    #         # # compute mass matrix
    #         # mass_contribution_1 = shape.T.dot(shape)*gauss_weights[iGauss]*np.linalg.det(J)*h
    #         # mass[element_node_id, element_node_id] += mass_contribution_1

    #         # mass_contribution_2 = shape.T.dot(shape)*dens*gauss_weights[iGauss]*np.linalg.det(J)*h
    #         # mass[element_node_id+nP, element_node_id+nP] += mass_contribution_2

    #         # stiff_contribution = np.dot(np.dot(B.T, C), B) * h * gauss_weights[iGauss] * np.linalg.det(J)
    #         # stiff[np.ix_(ele_dof, ele_dof)] += stiff_contribution

    #         stiff[np.ix_(ele_dof, ele_dof)] += np.dot(np.dot(B.T, C), B) * h * gauss_[q] * np.linalg.det(J)

    #         # compute mass matrix
    #         # shape_T = shape.T
    #         # mass_contribution_1 = np.dot(shape_T, shape) * h * gauss_weights[iGauss] * np.linalg.det(J)
    #         # mass[element_node_id, element_node_id] += mass_contribution_1

    #         # mass_contribution_2 = np.dot(shape_T, shape) * dens * h * gauss_weights[iGauss] * np.linalg.det(J)
    #         # mass[element_node_id + nP, element_node_id+ nP] += mass_contribution_2

    #         mass[np.ix_(id, id)] += np.outer(shape, shape) * dens * h * gaussWt[q] * np.linalg.det(J)
    #         mass[np.ix_(id + nP, id + nP)] += np.outer(shape, shape) * dens * h * gaussWt[q] * np.linalg.det(J)


    number_of_Gauss_points_per_direction = 2
    [gaussLoc,gaussWt] = Gauss_Quadrature(number_of_Gauss_points_per_direction)

    for e in range(nE):
        id = elNode[e, :]
        elDof = np.hstack([id, id + nP])

        ndof = len(id)  # ndof = 4 for Q4

        for q in range(gaussWt.shape[0]):
            GaussPoint = gaussLoc[q, :]
            xi, eta = GaussPoint[0], GaussPoint[1]

            shape, nDeriva = shapeFuncQ4(xi, eta)
            J, xyDeriva = Jacobian(xy[id, :], nDeriva)

            B = np.zeros((3, 2 * ndof))
            B[0, :ndof] = xyDeriva[:, 0]
            B[1, ndof:2*ndof] = xyDeriva[:, 1]
            B[2, :ndof] = xyDeriva[:, 1]
            B[2, ndof:2*ndof] = xyDeriva[:, 0]

            stiff[np.ix_(elDof, elDof)] += np.dot(np.dot(B.T, C), B) * h * gaussWt[q] * np.linalg.det(J)
            
            mass[np.ix_(id, id)] += np.outer(shape, shape) * dens * h * gaussWt[q] * np.linalg.det(J)
            mass[np.ix_(id + nP, id + nP)] += np.outer(shape, shape) * dens * h * gaussWt[q] * np.linalg.det(J)


            


                      


    return stiff , mass,B