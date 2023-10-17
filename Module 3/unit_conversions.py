# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Peter Phan
# Olivia Goralski
# Claudia Phan
# Benjamin Sandefur
# Section: 521
# Assignment: Lab 3.15
# Date: 1 September 2023

# Define Functions
def pounds_to_newtons(pounds):
    return pounds * 4.44822

def meters_to_feet(meters):
    return meters * 3.28084

def atm_to_kPa(atm):
    return atm * 101.325

def watts_to_btu(watts):
    return watts * 3.412142

def liters_to_gallons(liters):
    return liters * 15.8503231

def celcius_to_farenheit(celcius):
    return (celcius * 9 / 5) + 32

quantity = float(input('Please enter the quantity to be converted: '))
print(f'{quantity:.2f} pounds force is equivalent to {pounds_to_newtons(quantity):.2f} Newtons')
print(f'{quantity:.2f} meters is equivalent to {meters_to_feet(quantity):.2f} feet')
print(f'{quantity:.2f} atmospheres is equivalent to {atm_to_kPa(quantity):.2f} kilopascals')
print(f'{quantity:.2f} watts is equivalent to {watts_to_btu(quantity):.2f} BTU per hour')
print(f'{quantity:.2f} liters per second is equivalent to {liters_to_gallons(quantity):.2f} US gallons per minute')
print(f'{quantity:.2f} degrees Celsius is equivalent to {celcius_to_farenheit(quantity):.2f} degrees Fahrenheit')

