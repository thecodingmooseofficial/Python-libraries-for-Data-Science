import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
data = np.random.rand(10, 10)

# Create a heatmap
plt.imshow(data, cmap='viridis', interpolation='nearest')
plt.colorbar(label='Intensity')

# Add title
plt.title('Heatmap')

# Display the plot
plt.show()
