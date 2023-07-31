import csv
from datetime import datetime

#Opening Sitka File
sitka = csv.reader(open("sitka_weather_2018_simple.csv", 'r'))
sitkaHeader = next(sitka)
sitkaLowIndex = 0
sitkaHighIndex = 0
sitkaDateIndex = 0 
sitkaNameIndex = 0
sitkaName = ''

#Opening Death Valley File
death = csv.reader(open("death_valley_2018_simple.csv", 'r'))
deathHeader = next(death)
deathLowIndex = 0
deathHighIndex = 0
deathDateIndex = 0
deathNameIndex = 0
deathName = ''

#Set the hig and lows index for both files
for index, (sHeader, dHeader) in enumerate(zip(sitkaHeader, deathHeader)):
    if sHeader == "NAME":
        sitkaNameIndex = index
    elif sHeader == "TMIN":
        sitkaLowIndex = index
    elif sHeader == "TMAX":
        sitkaHighIndex = index
    elif sHeader == "DATE":
        sitkaDateIndex = index
    elif sHeader == "Name":
        sitkaNameIndex = index

    if dHeader == "NAME":
        deathNameIndex = index
    elif dHeader == "TMIN":
        deathLowIndex = index
    elif dHeader == "TMAX":
        deathHighIndex = index
    elif dHeader == "DATE":
        deathDateIndex = index

sitkaLows, sitkaHighs, sitkaDates = [],[],[]
deathLows, deathHighs, deathDates = [],[],[]

for value in sitka:
    try:
        dateVal = datetime.strptime(value[sitkaDateIndex], '%Y-%m-%d')
        high = int(value[sitkaHighIndex])
        low = int(value[sitkaLowIndex])
    except ValueError:
        print(f"Missing data for {value}")
    else:
        sitkaDates.append(dateVal)
        sitkaHighs.append(high)
        sitkaLows.append(low)
    sitkaName = value[sitkaNameIndex]

for value in death:
    try:
        dateVal = datetime.strptime(value[deathDateIndex], '%Y-%m-%d')
        high = int(value[deathHighIndex])
        low = int(value[deathLowIndex])
    except ValueError:
        print(f"Missing data for {value}")
    else:
        deathDates.append(dateVal)
        deathHighs.append(high)
        deathLows.append(low)
    deathName = value[deathNameIndex]    

def generateTitle(x,y):
    title = "Temperature comparison between " + x + " and " + y 
    return title


import matplotlib.pyplot as plt
fig = plt.figure()

plt.suptitle(generateTitle(sitkaName, deathName), fontsize = 10)

plt.subplot(2,1,1) # Sitka plot
plt.plot(sitkaDates, sitkaHighs, c='red')
plt.plot(sitkaDates, sitkaLows, c='blue')
plt.fill_between(sitkaDates, sitkaHighs, sitkaLows, facecolor = 'blue', alpha = 0.1)
plt.title(sitkaName, fontsize = 8)


plt.subplot(2,1,2) # Death plot
plt.plot(deathDates, deathHighs, c='red')
plt.plot(deathDates, deathLows, c='blue')
plt.fill_between(deathDates, deathHighs, deathLows, facecolor = 'blue', alpha = 0.1)
plt.title(deathName, fontsize = 8)

fig.autofmt_xdate()
plt.show()


