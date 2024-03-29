import numpy as np
import scipy.linalg as la


def solve_for_stress(displacements, elementNodes, element_coordinates, constitutiveMat, StrainDispMat):
    num_elements = len(elementNodes)
    stresses = np.zeros((num_elements, 3))
    for i, element in enumerate(elementNodes):
        element_displacements = np.array([])
        u_disp_index = element
        v_disp_index = [x + len(elementNodes) for x in element]
        coordinates = element_coordinates[element,:]
        uDisp = displacements[u_disp_index]
        print('uDisp=',uDisp)
        vDisp = displacements[v_disp_index]
        print('vDisp=',vDisp)
        element_displacements = np.append(uDisp, vDisp)
        # for j in range(len(uDisp)):
            
        #     uvDisp = np.array([uDisp[j], vDisp[j]])
        #     element_displacements = np.append(element_displacements, uvDisp)
            
        print('element_displacements=',element_displacements)
        stress = constitutiveMat @ StrainDispMat @ element_displacements
        print('stress=',stress)
        stresses[i] = stress


    return stresses