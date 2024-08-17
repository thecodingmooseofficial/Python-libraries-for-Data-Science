import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10] 

# Create a line plot with custom styles
plt.plot(x, y1, label='Dashed Line with Squares', linestyle='--', marker='s', color='blue')
plt.plot(x, y2, label='Dotted Line with Triangles', linestyle=':', marker='^', color='green') 

# Add labels, title, legend, and grid
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot with Different Styles')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
