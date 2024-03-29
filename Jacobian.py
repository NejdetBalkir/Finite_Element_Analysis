import numpy as np
import math

def Jacobian(nodeCoord, nDeriva):
    # J: Jacobian matrix
    # xyDeriva: derivatives with respect to x and y

    J = np.dot(nodeCoord.T, nDeriva)

    xyDeriva = np.dot(nDeriva, np.linalg.inv(J))

    return J, xyDeriva




