import numpy as np
import matplotlib.pyplot as plt

# Create sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
plt.plot(x, y, color='red')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Sine of X')
plt.title('Plot from NumPy Array')

# Display the plot
plt.show()
