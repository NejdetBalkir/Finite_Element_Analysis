import numpy as np
from solution import solution
from QuadrilateralMesh import QuadrilateralMesh
from PlotMesh import PlotMesh
from ShapeFunction import shapeFuncQ4
from StiffnessQuad import StiffnessMatrix

# Tolerance
tol = 1e-5

# Material properties
E = 2e11  # Elastic modulus
pois = 0.27  # Poisson's ratio
dens = 7850  # Mass density

# Stress-strain matrix for Plane stress condition
C = E / (1 - pois ** 2) * np.array([[1, pois, 0], 
                                    [pois, 1, 0], 
                                    [0, 0, (1 - pois) / 2]])

# Geometrical properties
Lx, Ly, h = 2, 2, 0.01  # Dimensions and plate thickness
nx, ny = 2, 2  # Number of divisions in x and y directions
dx, dy = Lx / nx, Ly / ny  # Mesh size in x and y directions

# Create mesh using a custom function (to be implemented)
xy, elNode, nE, nP = QuadrilateralMesh(Lx, Ly, nx, ny)
nDof = 2 * nP  # Number of global degrees of freedom

# Plot mesh using a custom function (to be implemented)
# PlotMesh(xy, elNode)

# Boundary conditions
left = np.where(xy[:, 0] == 0)[0]
fixedDof = np.concatenate([left, left + nP])

# Loading conditions
fx, fy = 5e8, 0
force = np.zeros(nDof)
right = np.where(xy[:, 0] >= Lx)[0]
force[right] = fx * dy
force[right[0]] = fx * dy / 2
force[right[-1]] = fx * dy / 2

# Calculate stiffness matrix using a custom function (to be implemented)
stiff, mass = StiffnessMatrix(nDof, nE, elNode, nP, xy, C, dens, h)

# Solve the equilibrium equation using a custom function (to be implemented)
disp = solution(nDof, fixedDof, stiff, force)

print(' determinant stiffness matrix = ', np.linalg.det(stiff))
print(' determinant mass matrix = ', np.linalg.det(mass))

print('displacement=', disp)


