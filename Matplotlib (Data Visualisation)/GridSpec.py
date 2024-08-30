import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(x / 10)
y4 = np.log(x + 1)

# Create a figure with GridSpec
fig = plt.figure(figsize=(12, 8))
gs = GridSpec(3, 3, width_ratios=[2, 1, 1], height_ratios=[1, 2, 1])

# Create subplots
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, :-1])
ax3 = fig.add_subplot(gs[1, -1])
ax4 = fig.add_subplot(gs[2, :])

# Plot data
ax1.plot(x, y1, color='blue')
ax1.set_title('Sine Wave')

ax2.plot(x, y2, color='red')
ax2.set_title('Cosine Wave')

ax3.plot(x, y3, color='green')
ax3.set_title('Exponential Function')

ax4.plot(x, y4, color='purple')
ax4.set_title('Logarithmic Function')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()