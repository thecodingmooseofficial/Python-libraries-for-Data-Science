import matplotlib.pyplot as plt
import numpy as np 

# Generate random data 
data = np.random.randn(1000) 

# Create a histogram 
plt.hist(data, bins=30, color='yellow', edgecolor='blue') 

# Add labels and title 
plt.xlabel('Value') 
plt.ylabel('Frequency') 
plt.title('Histogram Example')

# Display the plot
plt.show()
