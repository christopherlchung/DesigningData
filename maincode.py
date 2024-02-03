import csv
import matplotlib.pyplot as plt
import mplcursors

with open(file='phys sports participation.csv', newline='') as sportsPar:
    reader = csv.reader(sportsPar)
    sportParticipation = list(reader)

i = 0
newPart = []

while i < len(sportParticipation) and sportParticipation[i][0] != "Region":
    i += 1

regions_to_check = [
    "Newfoundland and Labrador", "Prince Edward Island", "Nova Scotia", "New Brunswick",
    "Quebec", "Ontario", "Manitoba", "Saskatchewan", "Alberta", "British Columbia",
    "Yukon", "Northwest Territories"
]

for region in regions_to_check:
    i = 0
    while i < len(sportParticipation):
        if sportParticipation[i][0] == region:
            newPart.append([sportParticipation[i][0], sportParticipation[i][1]])
            break
        i += 1

province = [entry[0] for entry in newPart]
percentage = [float(entry[1].rstrip('%')) for entry in newPart] # ".rstrip" is removing the percentage--this will allow the program to convert the quantity to a float.

# Define a color for each province
province_colors = {
    "Newfoundland and Labrador": 'blue',
    "Prince Edward Island": 'green',
    "Nova Scotia": 'red',
    "New Brunswick": 'purple',
    "Quebec": 'orange',
    "Ontario": 'pink',
    "Manitoba": 'brown',
    "Saskatchewan": 'cyan',
    "Alberta": 'magenta',
    "British Columbia": 'yellow',
    "Yukon": 'gray',
    "Northwest Territories": 'lime'
}

colors = [province_colors.get(p, 'black') for p in province]

plt.scatter(province, percentage, c=colors, s=1300, alpha=0.5, edgecolors='black', linewidth=3, zorder=6)

plt.grid(zorder=5)

plt.xlabel("Provinces")
plt.xticks(rotation=45, fontsize=10)
plt.ylabel("% of Youth Participate in Sport")
plt.title("Provincial Differences in Youth's Sport Participation in Canada")

def on_hover(sel):
    ind = sel.target.index
    province_name = province[ind]
    data_point = percentage[ind]
    label = f"{province_name}\n% Participation: {data_point:.2f}%"
    sel.annotation.set_text(label)

# Connect the hover event to the figure
mplcursors.cursor(hover=True).connect("add", on_hover)

plt.show()
