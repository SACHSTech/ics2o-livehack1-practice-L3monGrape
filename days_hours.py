"""
---------------------------------------------------------
Name: days_hours.py
Purpose: Lets you enter number of hours and converts it to number of days

Author: Yeh.A

Created: date in 08/02/2021
----------------------------------------------------------
"""
print("***** Hours to Days and Hours Converter *****")

print(" ")

#get number of hours from user
number_of_hours = int(input("Enter number of hours: "))

#calculate hours to days with remainder
hours_to_days = number_of_hours//24 
remaining_hours = number_of_hours % 24

#output days and hours
print("Number of Days:", hours_to_days, "day(s)", remaining_hours, "hour(s)")  