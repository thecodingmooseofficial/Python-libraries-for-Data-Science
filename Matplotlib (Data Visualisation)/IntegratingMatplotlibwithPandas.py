import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame from the data
data = {'x': [1, 2, 3, 4, 5], 'y': [2, 3, 5, 7, 11]}
df = pd.DataFrame(data)

# Create a line plot from the DataFrame
df.plot(x='x', y='y', kind='line', title='Line Plot from DataFrame')

# Set the labels
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()