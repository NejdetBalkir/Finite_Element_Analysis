# THIS CODE CALCULATES THE GAUSS POINTS AND GAUSS WEIGHTS #

import numpy as np

def Gauss_Quadrature(n):
    # PURPOSE:
    #     THIS FUNCTION CALCULATES THE GAUSS POINTS AND GAUSS WEIGHTS
    # INPUTS:
    #     n : number of gauss points per direction
    # OUTPUTS:
    #     gauss_points : gauss points
    #     gauss_weights : gauss weights
    # '''

    if n == 1:
        gauss_points = np.array([0.0, 0.0])
        gauss_weights = np.array([4.0])
    elif n ==2:
        gauss_points = np.array([ [-0.577350269189626, -0.577350269189626],
                           [0.577350269189626, -0.577350269189626],
                           [0.577350269189626, 0.577350269189626],
                           [-0.577350269189626, 0.577350269189626] ],
                                )
        gauss_weights = np.array([[1.0], [1.0], [1.0], [1.0]])

    return gauss_points, gauss_weights
