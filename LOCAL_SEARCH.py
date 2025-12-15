# Ackley multimodal function

import numpy as np
from numpy import exp, sqrt, cos, e, pi
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Objective function
def objective(x, y):
    return (
        -20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2)))
        - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y)))
        + e + 20
    )

# Define range for input
r_min, r_max = -5.0, 5.0

# Sample input range uniformly
xaxis = np.arange(r_min, r_max, 0.1)
yaxis = np.arange(r_min, r_max, 0.1)

# Create meshgrid
x, y = np.meshgrid(xaxis, yaxis)

# Compute results
results = objective(x, y)

# Create 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, results, cmap='jet')

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Ackley Function")

# Show plot
plt.show()

