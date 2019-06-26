#Imports
import datetime

#Initial
number_sundays = 0

#Run Through Years
for year in range(1, 101):
    #Run Through Months
    for month in range(1, 13):
        #Find Day
        day = datetime.date(1900 + year, month, 1)

        #Count Sundays
        if day.weekday() == 6:
            number_sundays += 1

#Output
print number_sundays
