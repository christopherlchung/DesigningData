import csv
import matplotlib.pyplot as plt
import numpy as np

with open("test.csv") as data_tv:
    reader = csv.reader(data_tv)
    datatv = list(reader)

i = 1
newsData = []
docData = []
infoData = []
sportData = []
musicData = []
gameData = []
genData = []

while i < len(datatv):
    if "News" in datatv[i][0]:
        newsData.append(datatv[i][1:5])

    elif "Long-form documentary" in datatv[i][0]:
        docData.append(datatv[i][1:5])

    elif "Other informational" in datatv[i][0]:
        infoData.append(datatv[i][1:5])

    elif "Sports" in datatv[i][0]:
        sportData.append([float(value.replace('#', '')) for value in datatv[i][1:5]])

    elif "Music, dance, and variety" in datatv[i][0]:
        musicData.append(datatv[i][1:5])

    elif "Game show" in datatv[i][0]:
        gameData.append(datatv[i][1:5])
    
    elif "General entertainment/ Human interest/ Reality" in datatv[i][0]:
        genData.append(datatv[i][1:5])

    i += 1

categories = ["News", "Long-form documentary", "Other informational", "Sports", "Music, dance, and variety", "Game show", "General entertainment/ Human interest/ Reality"]
years = ["2009-2010", "2010-2011", "2011-2012", "2012-2013"]

# Listing data values extracted from from 2009 to 2013
data = {
    "News": [float(value) for entry in newsData for value in entry],
    "Long-form documentary": [float(value) for entry in docData for value in entry],
    "Other informational": [float(value) for entry in infoData for value in entry],
    "Sports": [float(value) for entry in sportData for value in entry],
    "Music, dance, and variety": [float(value) for entry in musicData for value in entry],
    "Game show": [float(value) for entry in gameData for value in entry],
    "General entertainment/ Human interest/ Reality": [float(value) for entry in genData for value in entry]
}

# Set up the bar chart
bar_width = 0.1
bar_positions = np.arange(len(years))

# Plot each category
for i, category in enumerate(categories):
    # Calculate the x-positions for each category
    x_positions = [pos + bar_width * i for pos in bar_positions]

    # Set zorder for consistent layering
    z_order = 7 if category == "Sports" else 6

    # Plot the bars for the current category
    plt.bar(
        x_positions,
        data[category],
        width=bar_width,
        label=category,
        color="maroon" if category == "News" else
              "brown" if category == "Long-form documentary" else
              "red" if category == "Sports" else
              "indianred" if category == "Other informational" else
              "tomato" if category == "Music, dance, and variety" else
              "lightcoral" if category == "Game show" else
              "darksalmon",
        edgecolor="black" if category == "Sports" else None,  
        linewidth=4 if category == "Sports" else None,  
        zorder=z_order
    )

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Viewing Hours (millions)')
plt.title('Average Weekly Viewing Hours for Canadian Television Programs')

# Display legend, upper right
legend = plt.legend(loc='upper right')

# Set x-axis ticks and labels
plt.xticks(bar_positions + (len(categories) - 1) * bar_width / 2, years)

# Set the z-order of the legend
legend.set_zorder(7)

# Add a grid to the background of the bar graph
plt.grid(axis='y', zorder=5)

# Show the plot
plt.show()
