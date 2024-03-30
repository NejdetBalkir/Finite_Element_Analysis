import numpy as np
import math

def QuadrilateralMesh(Lx,Ly,nx,ny):
    # Definition:
        # This function generates a mesh for the given 2D boundary
    # Inputs:
    #     Lx : Length of the boundary in x direction
    #     Ly : Length of the boundary in y direction
    #     nx : number of elements in x direction
    #     ny : number of elements in y direction
    # Outputs:
    #     coordinates : coordinates of the mesh nodes
    #         coordinates = [node x y]
    #     nodes : nodal connectivity of the elements
    #         nodes = [node1 node2 ...]
    #     nel : number of elements
    #     nnodes : total number of nodes

    nel = nx * ny   # number of elements
    nnel = 4        # number of nodes per element

    # Assume dividing a line into n pieces, there will be (n+1) nodes
    nonx = nx + 1
    nony = ny + 1

    nnode = nonx * nony     # total number of nodes

    # discretizing the x and y direction of the boundary 

    dnx = np.linspace(0,Lx,nonx) # discretize the x direction
    dny = np.linspace(0,Ly,nony) # discretize the y direction


    xx, yy = np.meshgrid(dnx, dny) # create a mesh grid of xx and yy

    coordinates = np.column_stack((xx.ravel(), yy.ravel()))

    ## CREATING NODAL CONNECTIVITY MATRIX #

  # Create NodeNo array from 1 to nnode
    NodeNo = np.arange(1, nnode + 1)

    # Initialize nodes matrix with zeros
    nodes = np.zeros((nel, nnel))

    # Reshape NodeNo into a 2D array
    NodeNo = NodeNo.reshape(nonx, nony)

    # Select nodal point numbers for specific elements
    nodes[:, 0] = NodeNo[:nony-1, :nonx-1].reshape(nel)
    nodes[:, 1] = NodeNo[:nony-1, 1:nonx].reshape(nel)
    nodes[:, 2] = NodeNo[1:nony, 1:nonx].reshape(nel)
    nodes[:, 3] = NodeNo[1:nony, :nonx-1].reshape(nel)

    # Initialize X and Y arrays with zeros
    X = np.zeros((nnel, nel))
    Y = np.zeros((nnel, nel))

    for iel in range(nel):
        # Extract X and Y coordinates for the nodes of the current element
        X[:, iel] = coordinates[nodes[iel, :], 0]
        Y[:, iel] = coordinates[nodes[iel, :], 1]


    return coordinates, nodes, nel, nnode