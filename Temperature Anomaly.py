# Import csv file
import csv 

# Import matplotlib
import matplotlib.pyplot as plt

# Bring in csv file
with open("temperature-anomaly.csv", newline='') as tempData:
    reader = csv.reader(tempData)
    globalTempData = list(reader)

i = 1
gTemperature = [] # New list (list of lists)

while i < len(globalTempData):
    if globalTempData[i][0] == "Global":
        gTemperature.append([globalTempData[i][0], globalTempData[i][2], globalTempData[i][3], globalTempData[i][4], globalTempData[i][5]])
    i += 1

# Print the new/modified list
for temp in gTemperature:
    print(temp)

# Extract data
years = [entry[1] for entry in gTemperature]
avg = [float(entry[2]) for entry in gTemperature]
high = [float(entry[3]) for entry in gTemperature]
low = [float(entry[4]) for entry in gTemperature]

# Create line graph
# Perhaps change average line to purple ?
plt.plot(years, avg, label='Average Temperature', color='Grey', linewidth=3, zorder=2.5)  # Set a higher linewidth for boldness
plt.plot(years, high, label='Highest Temperature (Average)', color='Red', zorder=2, alpha=0.5)
plt.plot(years, low, label='Lowest Temperature (Average)', color='deepskyblue', zorder=1, alpha=0.5)

# To control the layering of lines in a Matplotlib plot, 
# we can use the zorder parameter. The zorder parameter 
# determines the drawing order of the elements, where higher 
# values are drawn on top of lower values. 
# We can assign different zorder values to each line 
# to control their stacking order.


# Add labels and title
plt.xlabel('Year')
plt.ylabel('Temperature Change (in degrees Celsius)')
plt.title('Global Temperature Anomaly, 1850 - 2023')

# Set x-axis ticks for every 10 years
plt.xticks(years[::10])

plt.grid(axis='y') # "axis='y'" ensures that only horizantal grid lines are displayed

# Display legend
plt.legend()

# Show the plot
plt.show()