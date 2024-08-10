#Case - Median Salary for a developer based on their age
from matplotlib import pyplot as plt

plt.style.available #for Built-in styles
print(plt.style.available) #Check terminal for output
plt.style.use('fivethirtyeight') #provides default colors and styles

'''
plt.xkcd() #xkcd comics style
'''

# Ages 18 to 55
DeveloperAges = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

# Median Python Developer Salaries by Age
PythonDevSalaries = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666, 84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]
plt.plot(DeveloperAges, PythonDevSalaries, color = 'b', marker = '.', linewidth = 2, label = 'Python Developers')

# Median JavaScript Developer Salaries by Age
JavascriptDevSalaries = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000, 78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]
plt.plot(DeveloperAges, JavascriptDevSalaries, color = '#adad3b', marker = '.', linewidth = 3, label = 'Javascript Developers')

# Median Developer Salaries by Age
OverallDevSalaries = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232, 78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]
plt.plot(DeveloperAges, OverallDevSalaries, color = 'k', linestyle = '--', linewidth = 3, marker = '.',  label = 'All Developers') #Write color = '#444444' for hexadecimal approach


plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')
plt.grid(True) #To put in a Grid
plt.legend()
plt.tight_layout() #This method automatically adjusts plot parameters to give some padding
plt.savefig('Graph.png')
plt.show()
