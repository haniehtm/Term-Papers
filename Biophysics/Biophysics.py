# -*- coding: utf-8 -*-
"""Biof0 HW02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rJqkqLD7pWtPyi1l-1nBF_qtZzp6LxGg
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1  # Step length
tau = 1  # Time step
num_steps = 1000  # Number of time steps

# Initialize arrays to store positions and squared positions
positions = np.zeros(num_steps + 1)
squared_positions = np.zeros(num_steps + 1)

# Perform random walk
for i in range(1, num_steps + 1):
    # Randomly choose direction (left or right)
    step = np.random.choice([-1, 1])
    # Update position
    positions[i] = positions[i - 1] + step * L
    # Calculate squared position
    squared_positions[i] = positions[i] ** 2

# Time array
time = np.arange(0, (num_steps + 1) * tau, tau)

# Plot movement path
plt.figure(figsize=(10, 5))
plt.plot(time, positions, color='blue')
plt.title('Movement Path of the Wanderer')
plt.xlabel('Time')
plt.ylabel('Position (x)')
plt.grid(True)
plt.show()

# Plot squared location
plt.figure(figsize=(10, 5))
plt.plot(time, squared_positions, color='red')
plt.title('Squared Location of the Wanderer')
plt.xlabel('Time')
plt.ylabel('Squared Location (x^2)')
plt.grid(True)
plt.show()

from scipy.stats import linregress

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(time, squared_positions)

# Calculate diffusion coefficient D
D = slope / 2

print("Diffusion Coefficient D:", D)

import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1  # Step length
tau = 1  # Time step
num_steps = 1000  # Number of time steps
num_walks = 10  # Number of random walks

# Initialize arrays to store positions
positions = np.zeros((num_walks, num_steps + 1))

# Perform multiple random walks
for i in range(num_walks):
    # Initialize position for each walk
    positions[i, 0] = 0
    for j in range(1, num_steps + 1):
        # Randomly choose direction (left or right)
        step = np.random.choice([-1, 1])
        # Update position
        positions[i, j] = positions[i, j - 1] + step * L

# Time array
time = np.arange(0, (num_steps + 1) * tau, tau)

# Plot movement paths
plt.figure(figsize=(10, 5))
for i in range(num_walks):
    plt.plot(time, positions[i], alpha=0.3)  # Set alpha for transparency

plt.title('Movement Paths of Random Walk Ensemble')
plt.xlabel('Time')
plt.ylabel('Position (x)')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1  # Step length
tau = 1  # Time step
num_steps = 1000  # Number of time steps
num_walks = 1000  # Number of random walks

# Initialize arrays to store squared positions
squared_positions = np.zeros((num_walks, num_steps + 1))

# Perform multiple random walks
for i in range(num_walks):
    position = 0
    for j in range(1, num_steps + 1):
        # Randomly choose direction (left or right)
        step = np.random.choice([-1, 1])
        # Update position
        position += step * L
        # Calculate squared position
        squared_positions[i, j] = position ** 2

# Calculate mean squared position across all walks
mean_squared_position = np.mean(squared_positions, axis=0)

# Time array
time = np.arange(0, (num_steps + 1) * tau, tau)

# Calculate the function 2Dt
D = L**2 / (2 * tau)
function_2Dt = 2 * D * time

# Plot mean squared position and 2Dt
plt.figure(figsize=(10, 5))
plt.plot(time, mean_squared_position, label='⟨x^2(t)⟩')
plt.plot(time, function_2Dt, label='2Dt', linestyle='--')
plt.title('Mean Squared Position vs. 2Dt')
plt.xlabel('Time')
plt.ylabel('Mean Squared Position / 2Dt')
plt.legend()
plt.grid(True)
plt.show()