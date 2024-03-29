# This function calculates the shape function for quadrilateral element in Finite Element Analysis

import numpy as np
import math

def shapeFuncQ4(xi, eta):
    # shape function and derivatives for Q4 elements
    # shape : Shape functions
    # nDeriva: derivatives with respect to xi and eta 
    # xi, eta: natural coordinates (-1 ... +1)
    
    shape = 1/4 * np.array([(1 - xi) * (1 - eta),
                            (1 + xi) * (1 - eta),
                            (1 + xi) * (1 + eta),
                            (1 - xi) * (1 + eta)])
    
    nDeriva = 1/4 * np.array([[-(1 - eta),    -(1 - xi)],
                              [1 - eta,       -(1 + xi)],
                              [1 + eta,        1 + xi],
                              [-(1 + eta),     1 - xi]])
    
    return shape, nDeriva