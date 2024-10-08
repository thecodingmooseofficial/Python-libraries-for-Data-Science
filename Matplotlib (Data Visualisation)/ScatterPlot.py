import matplotlib.pyplot as plt
import random

# Generate random sample data
x = [random.randint(1, 50) for data in range(50)]
y = [random.randint(1, 50) for data in range(50)]

# Use plt.scatter() to create a scatter plot with x and y data points
plt.scatter(x, y, color='green', marker='x')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')

# Display the plot
plt.show()
