import pandas as pd  # Pandas simplifies data manipulation and analysis with DataFrames
import matplotlib.pyplot as plt

# Load data from a CSV file using Pandas
data = pd.read_csv('data.csv')

# Display the first few rows of the data
print(data.head())

# Plot the data
plt.plot(data['x'], data['y'], marker='o')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot from CSV Data')

# Display the plot
plt.show()
