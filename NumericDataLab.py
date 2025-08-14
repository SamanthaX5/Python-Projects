#Samantha Belanger - Lab 3 - CST8279
#This calculates how many days are in 2023

from datetime import date

#Start/End of year
start_of_year = date(2023,1,1)
end_of_year = date(2023,12,31)

#Calculate how many days
num_days = (end_of_year - start_of_year).days + 1

#string function for output
print("There are this many days in 2023:" + str(num_days))
