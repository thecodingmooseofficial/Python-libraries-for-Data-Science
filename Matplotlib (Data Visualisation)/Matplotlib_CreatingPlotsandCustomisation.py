#Case - Median Salary for a developer based on their age
from matplotlib import pyplot as plt

plt.style.available #for Built-in styles
print(plt.style.available) #Check terminal for output
plt.style.use('fivethirtyeight') #provides default colors and styles

'''
plt.xkcd() #xkcd comics style
'''

# Ages 25 to 35
DeveloperAges = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# Median Python Developer Salaries by Age
PythonDevSalaries = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(DeveloperAges, PythonDevSalaries, color = 'b', marker = '.', linewidth = 2, label = 'Python Developers')

# Median JavaScript Developer Salaries by Age
JavascriptDevSalaries = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(DeveloperAges, JavascriptDevSalaries, color = '#adad3b', marker = '.', linewidth = 3, label = 'Javascript Developers')

# Median Developer Salaries by Age
OverallDevSalaries = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(DeveloperAges, OverallDevSalaries, color = 'k', linestyle = '--', linewidth = 3, marker = '.',  label = 'All Developers') #Write color = '#444444' for hexadecimal approach


plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')
plt.grid(True) #To put in a Grid
plt.legend()
plt.tight_layout() #This method automatically adjusts plot parameters to give some padding
plt.savefig('Matplotlib_CreatingPlotsandCustomization.png')
plt.show()
