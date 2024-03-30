import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
from matplotlib.colors import ListedColormap

def PlotFieldonMesh(coordinates, nodes, vari, varimin, varimax):
    # Setting color map similar to MATLAB's one
    cmap = np.array([[0, 0, 1],
                     [0, 0.25, 0.75],
                     [0, 0.5, 0.5],
                     [0, 0.75, 0.25],
                     [0, 1, 0],
                     [0.25, 1, 0],
                     [0.5, 1, 0],
                     [0.75, 1, 0],
                     [1, 1, 0],
                     [1, 0.75, 0],
                     [1, 0.5, 0],
                     [1, 0.25, 0],
                     [1, 0, 0]])

    nel = len(nodes)  # number of elements
    nnel = 4  # number of nodes per element

    # Initialization of the required matrices
    X = np.zeros((nnel, nel))
    Y = np.zeros((nnel, nel))
    profile = np.zeros((nnel, nel))

    for iel in range(nel):
        for i in range(nnel):
            nd = nodes[iel, i]  # extract connected node for (iel)-th element
            X[i, iel] = coordinates[nd, 0]  # extract x value of the node
            Y[i, iel] = coordinates[nd, 1]  # extract y value of the node
        profile[:, iel] = vari[nodes[iel,:]]  # extract component value of the node

    # Plotting the FEM mesh and profile of the given component
    # verts = [list(zip(X[:, i], Y[:, i])) for i in range(nel)]
    verts = []
    for iel in range(nel):
        verts.append([coordinates[n] for n in nodes[iel]])
    
    custom_cmap = ListedColormap(cmap)
    fig, ax = plt.subplots()
    poly = PolyCollection(verts, array=vari[nodes].mean(1), cmap=custom_cmap, edgecolors='None')
    ax.add_collection(poly)
    ax.autoscale_view()
    # plt.colorbar(poly, ax=ax, boundaries=np.linspace(varimin, varimax, len(custom_cmap.colors)))

    #Colorbar settings
    cbar = plt.colorbar(poly, ax=ax)
    ncolor = len(cmap)
    varistep = (varimax - varimin) / (ncolor - 1)
    cbar.set_ticks(np.arange(varimin, varimax + varistep, varistep))
    cbar.set_ticklabels([f'{i:.2f}' for i in np.arange(varimin, varimax + varistep, varistep)])

    # View settings
    plt.axis('equal')
    plt.axis('off')
    plt.show()

# Example usage
# coordinates = np.array([[x1, y1], [x2, y2], ...])
# nodes = np.array([[node1, node2, node3], ...]) for each element
# vari = np.array([value1, value2, ...]) corresponding to each node
# varimin = min(vari)
# varimax = max(vari)
# PlotFieldonMesh(coordinates, nodes, vari, varimin, varimax)
