import pandas as pd
import matplotlib.pyplot as plt

# Load data from a CSV file
data = pd.read_csv('Data.csv')

# Filter data where 'Category' is 'A'
filtered_data = data[data['Category'] == 'A']

# Group data by 'Month' and calculate the mean of 'Value'
grouped_data = filtered_data.groupby('Month')['Value'].mean()

# Plot the grouped data
grouped_data.plot(kind='bar', color='yellow')

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Average Value')
plt.title('Average Value by Month for Category A')

# Display the plot
plt.show()

