
import csv
from datetime import datetime


sitka = open("sitka_weather_2018_simple.csv", 'r')
sitkaFile = csv.reader(sitka)
header_row = next(sitkaFile)

for index, col_header in enumerate(header_row):
    print(index, col_header)

highs = []
dates = []
lows = []

# We want to convert the date string into a date object, %Y = year %m = month %d = day
some_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(some_date)

for value in sitkaFile:
    highs.append(int(value[5]))
    dateVal = datetime.strptime(value[2], '%Y-%m-%d')
    dates.append(dateVal)

    lowVal = int(value[6])
    lows.append(lowVal)
    

# print(highs[:5]) # From 0 to 4
# print(dates)
# print(lows)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c='red', alpha = 0.5) # The argument (in this case 'dates' and 'highs') has to be a list of values
plt.plot(dates, lows, c = 'blue', alpha = 0.5) # Alpha changes the boldness of the line

plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1) #Fill on x-value between y1 and y2

plt.title("Daily Low and High Temps, 2018", fontsize=16)
plt.xlabel("Dates", fontsize=16)
plt.ylabel("Temps in (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()
plt.show()