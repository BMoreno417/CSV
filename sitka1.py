import csv


sitka = open("sitka_weather_07-2018_simple.csv", 'r')
sitkaFile = csv.reader(sitka)
header_row = next(sitkaFile)

for index, col_header in enumerate(header_row):
    print(index, col_header)

highs = []

for temp in sitkaFile:
    highs.append(int(temp[5]))

print(highs[:5]) # From 0 to 4

import matplotlib.pyplot as plt

plt.plot(highs, c = 'red') # The argument (in this case 'highs') has to be a list of values
plt.title("Daily High Temps, July 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temps in (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.show()
