import numpy as np
import matplotlib.pyplot as plt

# --- 1. SETUP THE PIEZOELECTRIC DISC ---
# Create a grid representing the crystal surface
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Radius = np.sqrt(X**2 + Y**2)

# Mask: We only care about what happens INSIDE the disc radius
# (Setting outside values to NaN makes them invisible in the plot)
Mask = Radius <= 2.8

# --- 2. THE ACOUSTIC INPUT (TWO WAVES) ---
# To create rotation from vibration, we need two standing waves
# phase-shifted by 90 degrees (Pi/2).

# Frequency Mode (Try n=1 for a simple vortex, n=2 for double helix, n=4 for an Octopole)
n = 1
# n = 4

# Theta is the angle around the center
Theta = np.arctan2(Y, X)

# Wave 1: The "Real" component (Cos)
# This represents physical displacement at Time T=0
Wave_A = np.cos(n * Theta) * (Radius * np.exp(-Radius**2))

# Wave 2: The "Imaginary" component (Sin) - Phase Shifted
# This represents physical displacement at Time T=0.25
Wave_B = np.sin(n * Theta) * (Radius * np.exp(-Radius**2))

# --- 3. THE PIEZOELECTRIC CONVERSION ---
# In a piezo crystal, Stress (Vibration) creates Voltage (Potential).
# We simulate the Resulting Potential Field (V) at a specific moment
# by combining the waves to form a "Traveling Wave."
# Potential V ~ Wave_A + Wave_B (Simplified)

Potential = Wave_A - Wave_B  # Combining them to create the spiral phase

# --- 4. CALCULATE THE ELECTRIC FIELD ---
# The Electric Field (E) is the Gradient (Slope) of the Potential
# E = - Gradient(V)
Ex, Ey = np.gradient(-Potential)

# Apply the circular mask (cut off the corners)
Ex[~Mask] = np.nan
Ey[~Mask] = np.nan
Potential[~Mask] = np.nan

# --- 5. VISUALIZATION ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plot the Electric Potential (Voltage) as color
# High Voltage (Red) vs Low Voltage (Blue)
cplot = ax.contourf(X, Y, Potential, levels=40, cmap='twilight')
plt.colorbar(cplot, label='Piezoelectric Potential (Volts)')

# Plot the Electric Field Vectors (The Flow)
# If we see a SPIRAL, we have proven Acoustic Torsion.
strm = ax.streamplot(x, y, Ex, Ey, color='white', linewidth=1.2, density=1.5, arrowsize=1.5)

# Styling
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_title(f'The Acoustic Anode: Rotating Electric Field (Mode n={n})', color='black', fontsize=14)
plt.show()
