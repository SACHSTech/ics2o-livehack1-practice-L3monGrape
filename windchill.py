"""
--------------------------------------------------------
Name: windchill.py
Purpose: Lets you enter temperature in celsius and wind speed in km/h to calculate the windchill factor

Author: Yeh. A

Created: date in 08/02/2021
--------------------------------------------------------
"""
print("***** Windchill Calculator *****")

print(" ")

#get temperature and windspeed values from user
temp_C = float(input("Enter temperature in celsius: "))
windspeed = float(input("Enter windspeed in km/h: "))

#compute wind chill
wind_chill = 13.12 + (0.6215*temp_C) - (11.37 * windspeed**0.16) + (0.3965*temp_C * windspeed**0.16)

#output windchill
print("With the wind chill factor, it feels like", wind_chill, "°C outside.")