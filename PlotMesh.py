import numpy as np
import matplotlib.pyplot as plt

def PlotMesh(coordinates , nodes):

    # PURPOSE OF THE FUNCTION:
    #     -   PLOTTING THE FINITE ELEMENT MESH USING THE COORDINATES AND CONNECTIVITY CALCULATED IN THE
    #         QuadrilateralMesh FUNCTION.
    # INPUTS:
    #     -   coordinates     =   COORDINATES OF THE nodes
    #     -   nodes           =   INFORMATION OF NODES IN EACH ELEMENT

    number_of_elements = len(nodes)                # number of elements
    number_of_nodes_per_element = nodes.shape[1]           # number of nodes per element

    # X & Y matrices store the coordinates of the nodes
    # X = np.zeros((number_of_nodes_per_element, number_of_elements))
    # Y = np.zeros((number_of_nodes_per_element, number_of_elements))

    X = np.zeros((number_of_nodes_per_element + 1, number_of_elements))
    Y = np.zeros((number_of_nodes_per_element + 1, number_of_elements))


    for element in range(number_of_elements): # iterate over each element
        for snode in range(number_of_nodes_per_element):
            node_index = nodes[element,snode]
            X[snode,element] = coordinates[node_index,0]
            Y[snode,element] = coordinates[node_index,1]

        X[number_of_nodes_per_element, element] = X[0, element]
        Y[number_of_nodes_per_element, element] = Y[0, element]

    # Plot the finite element mesh
    plt.figure()
    for element in range(number_of_elements):
        plt.plot(X[:, element], Y[:, element], color='k')  # Plot element edges
        plt.fill(X[:, element], Y[:, element], 'w')       # Fill element with white color
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Finite Element Mesh')
    plt.grid(True)
    plt.axis('equal')  # Set equal aspect ratio
    plt.show()

    

    return
    