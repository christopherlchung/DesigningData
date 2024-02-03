import csv
import matplotlib.pyplot as plt

with open(file="Annual_Surface_Temperature_Change.csv", newline='') as tempChange:
    reader = csv.reader(tempChange)
    temperature = list(reader)

with open(file="Climate-related_Disasters_Frequency.csv", newline='') as disasterFreq:
    reader = csv.reader(disasterFreq)
    disaster = list(reader)

i = 1
t = 1
j = 10 # Column 10 is where the years start
k = 29 # Column 29 is where the years start
year = 1980

masterList = []

# 1. Look for canada row and svae in i
# 2. process the canada rows
# while disaster i == "Canada"
# 3. j= 
# k is the column of 1980 in the temperature file

while t < len(temperature) and temperature[t][1] != "Canada": # Keep going through list until we reach Canada
    t += 1

while i < len(disaster) and disaster[i][1] != "Canada": # Keep going through list until we reach Canada 
    i += 1

while i < len(disaster) and disaster[i][1] == "Canada":
    j = 10
    k = 29
    year = 1980
    while j < len(disaster[i]):
        masterList.append([year, disaster[i][j], temperature[t][k]])
        j += 1
        k += 1
        year += 1

    i += 1


year = [int(entry[0]) for entry in masterList]
natural = [float(entry[1]) if entry[1] != '' else float('nan') for entry in masterList] # 'nan' means Not a Number
temp = [float(entry[2]) if entry[2] != '' else float('nan') for entry in masterList]

fig, ax = plt.subplots()


ax.bar(year, natural, label='Natural Disaster', alpha=1, zorder=6)

ax2 = ax.twinx()
ax2.plot(year, temp, color='Red', alpha=0.75, linewidth=3, zorder=5)


plt.title('Average Temperature Change in Canada vs. # of Natural Disasters Occured (1980 - 2022)')
ax.set_xlabel('Year')
ax.set_ylabel('# of Natural Disasters Occured')
ax2.set_ylabel('Change in Temperature (Degrees Celcius)')

plt.tight_layout()

plt.grid(zorder=0)

plt.show()
