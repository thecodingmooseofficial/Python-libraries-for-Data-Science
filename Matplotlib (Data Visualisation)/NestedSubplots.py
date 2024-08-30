import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x / 10)

# Create a figure and outer subplot
fig = plt.figure(figsize=(10, 8))
outer_ax = fig.add_subplot(111)

# Create nested subplots
inner_ax1 = fig.add_axes([0.1, 0.6, 0.35, 0.3])
inner_ax2 = fig.add_axes([0.55, 0.6, 0.35, 0.3])
inner_ax3 = fig.add_axes([0.1, 0.2, 0.35, 0.3])
inner_ax4 = fig.add_axes([0.55, 0.2, 0.35, 0.3])

# Plot data
inner_ax1.plot(x, y1, color='blue')
inner_ax1.set_title('Sine Wave')

inner_ax2.plot(x, y2, color='red')
inner_ax2.set_title('Cosine Wave')

inner_ax3.plot(x, y3, color='green')
inner_ax3.set_title('Tangent Wave')
inner_ax3.set_ylim(-10, 10) # Limit y-axis to avoid extreme values

inner_ax4.plot(x, y4, color='purple')
inner_ax4.set_title('Exponential Function')

# Remove outer subplot content
outer_ax.axis('off')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()