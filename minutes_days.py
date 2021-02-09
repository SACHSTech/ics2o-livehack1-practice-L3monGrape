"""
Name: minutes_days.py
Purpose: Lets you enter number of minutes and converts it to time in days, hours, and minutes

Author: Yeh. A
Created: 08/02/2021

"""
#title of the converter
print("***** Minutes to Days Converter *****")

print(" ")

#get number of minutes
number_of_minutes = int(input("Enter number of minutes: "))

#calculate minutes to days, hours, and minutes
minutes_to_days = number_of_minutes//1440
remaining_hours = number_of_minutes % 1440//60
remaining_minutes = number_of_minutes % 1440 % 60

#output result
print("Number of Days:", minutes_to_days, "days", remaining_hours, "hours", remaining_minutes, "minutes")