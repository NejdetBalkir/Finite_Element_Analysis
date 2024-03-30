# THIS THE MAIN FE CODE #

import numpy as np
import math
from QuadrilateralMesh import QuadrilateralMesh  
from PlotMesh import PlotMesh

## GEOMETRICAL PROPERTIES ##

Lx = 1
Ly = 1
h = 0.01 # Plate thickness

nx = 4 # number of division in x-direction
ny = 4 # number of division in y-direction

coordinates,eleNode,noE,noP = QuadrilateralMesh(Lx,Ly,nx,ny)

#   coordinates   =  coordinatesof the nodes
#   eleNode       = nodes of the elements
#   noE           = number of nodes
#   noP           = number of points

# print(eleNode)
# print(len(eleNode))
# print(len(coordinates))
# print(coordinates)
# print(coordinates[1,0])
X,Y = PlotMesh(coordinates,eleNode)

# print(coordinates)