import numpy as np

def solution(nDof, fixedDof, K, force):
    # PURPOSE:
    #     This function solves the equilibrium equation
    # INPUTS:
    #     nDof : number of degrees of freedom
    #     fixedDof : indices of fixed degrees of freedom
    #     K : global stiffness matrix
    #     force : force vector
    # OUTPUTS:
    #     disp : displacement vector


    allDof = np.arange(nDof)

    # Identify active DOF (those not fixed)
    activeDof = np.setdiff1d(allDof, fixedDof)

    # Solve for displacements at active DOF
    U = np.linalg.solve(K[np.ix_(activeDof, activeDof)], force[activeDof])

    # Initialize displacement array with zeros
    disp = np.zeros(nDof)

    # Assign computed displacements to active DOF in the displacement array
    disp[activeDof] = U



    return disp