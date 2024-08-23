import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x,y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create a contour plot
plt.contour(X, Y, Z, levels=20, cmap='plasma')

# Add color bar and title
plt.colorbar(label='Z Value')
plt.title('Contour Plot')

# Display the plot
plt.show()