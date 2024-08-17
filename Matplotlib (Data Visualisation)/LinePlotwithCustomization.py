import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10] 

# Create a line plot
plt.plot(x, y1, label='Series 1', marker='o', color='blue')
plt.plot(x, y2, label='Series 2', linestyle='--', color='red') 

# Add labels, title, legend, and grid
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot with Customization')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
