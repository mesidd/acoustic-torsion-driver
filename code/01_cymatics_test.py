import numpy as np
import matplotlib.pyplot as plt

def chladni_pattern(n, m, num_points=500):
    x = np.linspace(-1, 1, num_points)
    y = np.linspace(-1, 1, num_points)
    X, Y = np.meshgrid(x, y)

    # --- THE FIX ---
    # We use ADDITION (+) instead of subtraction.
    # This prevents them from canceling out when n == m.
    # This creates the "Checkerboard" or "Net" patterns.
    Z = np.cos(n * np.pi * X) * np.cos(m * np.pi * Y) + \
        np.cos(m * np.pi * X) * np.cos(n * np.pi * Y)

    return X, Y, Z

# --- EXPERIMENT CONFIGURATION ---
modes = [(2, 2), (5, 5), (7, 11), (13, 13)]

# --- VISUALIZATION ---
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('The Geometry of Sound: Positive Superposition', fontsize=20, color='white')
fig.patch.set_facecolor('black')

for ax, (n, m) in zip(axes.flat, modes):
    X, Y, Z = chladni_pattern(n, m)
    
    # Visualizing the absolute value of the wave height
    ax.contourf(X, Y, np.abs(Z), levels=30, cmap='inferno')
    
    ax.set_title(f'Frequency Mode (n={n}, m={m})', color='white', fontsize=14)
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()
