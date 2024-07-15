'''Write a Python program that prints the calendar for a given month and year.'''

import calendar


year = int(input("Enter the year: "))


cal = calendar.TextCalendar(calendar.SUNDAY) #creates a text calendar object that will start each week on Sunday.

for month in range(1, 13):
       
        print(cal.formatmonth(year, month))
