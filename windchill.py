"""
Name: windchill.py
Purpose: Lets you enter temperature in celsius and wind speed in km/h to calculate the windchill factor

Author: Yeh. A
Created: 08/02/2021

"""
#collect temperature and windspeed values
T = int(input("Enter temperature in celsius: "))
V = int(input("Enter windspeed in km/h: "))

#formula for calculating wind chill
wind_chill = 13.12 + (0.6215*T) - (11.37 * V**0.16) + (0.3965*T * V**0.16)

#output result
print("Wind chill:", wind_chill, "degrees celsius")