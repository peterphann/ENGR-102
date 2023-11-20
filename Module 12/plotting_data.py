# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 12.14
# Date:         17 November 2023

import numpy as np
import matplotlib.pylab as plt

def month_data(month : int, days : list) -> dict:
  temperatures = []
  highs = []
  lows = []

  for day in days:
    date = day[0].split('/')
    if int(date[0]) != month:
      continue
    if day[4] != '':
      temperatures.append(float(day[4])) 
    if day[5] != '':
      highs.append(int(day[5])) 
    if day[6] != '':
      lows.append(int(day[6])) 

  avg_temp = sum(temperatures) / len(temperatures)

  return (avg_temp, max(highs), min(lows))

# Open csv file and get data
with open('WeatherDataCLL.csv') as file:
  file = file.read()
  days = file.split('\n')[1:]
  days = [day.split(',') for day in days]

# Isolate fields
highs = [int(day[5]) for day in days if day[5] != '']
wind_speeds = [float(day[1]) for day in days if day[1] != '']
scatter_points = [np.array([int(day[3]), float(day[2])]) for day in days if day[3] != '' and day[2] != '']
scatter_points = np.array(scatter_points)

# Plot 1 - Line Graph
fig, ax1 = plt.subplots()
p1 = ax1.plot(highs, color='r', label='Max Temp')
ax1.set_title('Maximum Temperature and Average Wind Speed')
ax1.set_xlabel('date')
ax1.set_ylabel('Maximum Temperature, F')

ax2 = ax1.twinx()
p2 = ax2.plot(wind_speeds, color='b', label='Avg Wind')
ax2.set_ylabel('Average wind speed, mph')

leg = p1 + p2
labs = [l.get_label() for l in leg]
ax2.legend(leg, labs, loc='lower left')

plt.show()

# Plot 2 - Histogram
fig2, ax2 = plt.subplots()
ax2.hist(wind_speeds, bins=29, color='g', edgecolor='black')
ax2.set_title('Histogram of Average Wind Speed')
ax2.set_xlabel('Average Wind Speed, mph')
ax2.set_ylabel('Number of days')

plt.show()

# Plot 3 - Scatterplot
fig3, ax3 = plt.subplots()
ax3.scatter(scatter_points[:,0], scatter_points[:,1], color='black', s=10)
ax3.set_title('Precipitation vs. Average Relative Humidity')
ax3.set_xlabel('Average Relative Humidity %')
ax3.set_ylabel('Precipitation (in)')
plt.show()

# Plot 4 - Line and Bar Graph
fig4, ax4 = plt.subplots()
temps = []
highs = []
lows = []
months = range(1, 13)
for month in months:
  data = month_data(month, days)
  temps.append(data[0])
  highs.append(data[1])
  lows.append(data[2])

ax4.bar(months, temps, color='y')
ax4.plot(months, highs, color='r', label='High T')
ax4.plot(months, lows, color='b', label='Low T')
ax4.set_title('Temperature by Month')
ax4.set_xlabel('Month')
ax4.xaxis.set_ticks(range(1,13))
ax4.set_ylabel('Average Temperature, F')
ax4.legend()

plt.show()