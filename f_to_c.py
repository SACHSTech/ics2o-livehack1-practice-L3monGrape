"""
Name: f_to_c.py
Purpose: Lets you enter a measure in degrees Fahrenheit and prints the result in a measure of degrees celsius. 

Author: Yeh. A
Created: 08/02/2021

"""
#title of the converter
print("***** Fahrenheit to Celsius Converter *****")

print(" ")

#get fahrenheit temperature 
fahrenheit = int(input("Enter temperature in degrees fahrenheit: ")) 

#calculate conversion
celsius = (fahrenheit - 32)*5/9

#output result
print("Temperature in degrees celsius:", celsius)