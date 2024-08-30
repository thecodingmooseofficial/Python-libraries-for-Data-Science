import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x / 10)

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot data
axs[0, 0].plot(x, y1, color='blue')
axs[0, 0].set_title('Sine Wave')

axs[0, 1].plot(x, y2, color='red')
axs[0, 1].set_title('Cosine Wave')

axs[1, 0].plot(x, y3, color='green')
axs[1, 0].set_title('Tangent Wave')
axs[1, 0].set_ylim(-10, 10) # Limit y-axis to avoid extreme values

axs[1, 1].plot(x, y4, color='purple')
axs[1, 1].set_title('Exponential Function')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()