import numpy as np
from ShapeFunction import shapeFuncQ4
from Jacobian import Jacobian

def formStiffness2D(nDof, nE, elNode, nP, xy, C, dens, h):

    stiff = np.zeros((nDof, nDof))
    mass = np.zeros((nDof, nDof))

    # # 2 by 2 quadrature
    # gaussWt = np.array([[1.0], [1.0]])
    # gaussLoc = np.array([[0.577350269189626, -0.577350269189626],
    #                      [-0.577350269189626, -0.577350269189626]])

    gaussLoc = np.array([ [-0.577350269189626, -0.577350269189626],
                            [0.577350269189626, -0.577350269189626],
                            [0.577350269189626, 0.577350269189626],
                            [-0.577350269189626, 0.577350269189626] ],
                                )
    gaussLoc = np.round(gaussLoc, 3)
    gaussWt = np.array([1.0, 1.0, 1.0, 1.0])
    gaussWt = np.round(gaussWt, 3) 

    for e in range(nE):
        id = elNode[e, :]
        elDof = np.hstack((id, id + nP))
        ndof = len(id)

        for q in range(gaussWt.shape[0]):
            xi, eta = gaussLoc[q]

            # shape functions and derivatives
            [shape,naturalDerivatives] = shapeFuncQ4(xi,eta)

            # Jacobian matrix, inverse of Jacobian
            J, xyDeriva = Jacobian(xy[id, :], naturalDerivatives)
            J = np.round(J, 3)

            # B matrix (Linear strain - displacement matrix)
            B = np.zeros((3, 2 * ndof))
            B[0, 0:ndof] = xyDeriva[:, 0]
            B[1, ndof:(2 * ndof)] = xyDeriva[:, 1]
            B[2, 0:ndof] = xyDeriva[:, 1]
            B[2, ndof:(2 * ndof)] = xyDeriva[:, 0]

            # stiffness matrix
            stiff[elDof[:, None], elDof] += np.round(np.dot(np.dot(B.T, C), B) * h * gaussWt[q] * np.linalg.det(J),4)

            # mass matrix
            mass[id[:, None], id] += np.dot(shape, shape.T) * dens * h * gaussWt[q] * np.linalg.det(J)
            mass[id[:, None] + nP, id + nP] += np.dot(shape, shape.T) * dens * h * gaussWt[q] * np.linalg.det(J)

    return stiff, mass, B
