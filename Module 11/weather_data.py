# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Peter Phan
# Section:      521
# Assignment:   Lab 11.13
# Date:         1 November 2023

months = {
  '1' : 'January',
  '2' : 'February',
  '3' : 'March',
  '4' : 'April',
  '5' : 'May',
  '6' : 'June',
  '7' : 'July',
  '8' : 'August',
  '9' : 'September',
  '10' : 'October',
  '11' : 'November',
  '12' : 'December'
}

def mean(list):
  '''Returns the mean of a list'''

  return sum(list) / len(list)

def get_date(date):
  '''Returns a tuple containing the month and year given a date formatted M/DD/YYYY'''

  # Split the date by / and return needed values
  split = date.split('/')
  return months[split[0]], split[2]

# Open csv file and get data
file = open('WeatherDataCLL.csv')
data = file.readlines()
days = [line.strip('\n') for line in data]
days = [line.split(',') for line in days][1:]
file.close()

# Use list comprehension to isolate the highs and low
lows = [int(day[6]) for day in days if day[6].isdigit()]
highs = [int(day[5]) for day in days if day[5].isdigit()]
minimum = min(lows)
maximum = max(highs)

print(f'10-year maximum temperature: {maximum} F')
print(f'10-year minimum temperature: {minimum} F')
  
# Prompt user for month and year
print()
month = input('Please enter a month: ')
year = input('Please enter a year: ')
print()

print(f'For {month} {year}:')
range_days = [day for day in days if get_date(day[0]) == (month, year)]

# Calculate means for the given date range
temperatures = [int(day[4]) for day in range_days if day[4].isdigit()]
mean_temp = mean(temperatures)
humidities = [int(day[3]) for day in range_days]
mean_humidities = mean(humidities)
wind_speeds = [float(day[1]) for day in range_days]
mean_wind = mean(wind_speeds)
precipitation = [100 if float(day[2]) > 0 else 0 for day in range_days]
percent_precip = mean(precipitation)

print(f'Mean average daily temperature: {mean_temp:.1f} F')
print(f'Mean relative humidity: {mean_humidities:.1f}%')
print(f'Mean daily wind speed: {mean_wind:.2f} mph')
print(f'Percentage of days with precipitation: {percent_precip:.1f}%')
