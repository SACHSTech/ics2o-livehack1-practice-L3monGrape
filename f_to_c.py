"""
---------------------------------------------------------
Name: f_to_c.py
Purpose: Lets you enter a measure in degrees Fahrenheit and prints the result in a measure of degrees celsius. 

Author: Yeh. A

Created: 08/02/2021
---------------------------------------------------------
"""
print("***** Fahrenheit to Celsius Converter *****")

print(" ")

#get fahrenheit temperature from user
fahrenheit_temp = float(input("Enter temperature in degrees fahrenheit: ")) 

#compute celsius
celsius_temp = (fahrenheit_temp - 32) * 5/9

#output celsius
print("Temperature in celsius:", celsius_temp, "°")