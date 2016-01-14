# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if year % 4 != 0:
    # Years that are not divisible by 4 can't be leap years
        return False
    elif year % 100 != 0:
    # Years that are divisible by 4 but not 100 are leap years
        return True
    elif year % 400 != 0:
    # Years that are divisible by 100 are not leap years 
    # unless they are divisible by 400
        return False
    else:
    # Then they are a leap year
        return True

#print isLeapYear(2000)

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    days = 0
    
    # Adds days from full years
    # Counts up from y1 to y2 not including the partial years y1 or y2
    for y in range(y1+1, y2):
        # Adds the days in the leap year to the total
        if isLeapYear(y) == True:
            days += 366
        # Adds the days in a normal year to the total
        else:
            days += 365
    
    # Adds days from full months of start year
    # Counts up from m1 to end of the year not including start month
    for m in range(m1+1, 12):
        # If start year is not a leap year, adds days 
        if isLeapYear(y1) == False:
            days += daysOfMonths[m]
        # If start year is a leap year, makes February 29 days then adds days
        else:
            daysOfMonths[1] == 29
            days += daysOfMonths[m]

    # Adds days from full months of end year
    # Counts up from start of the year to end month without counting end month
    for m in range(0, m2):
        # If end year is not a leap year, adds days 
        if isLeapYear(y2) == False:
            days += daysOfMonths[m]
        # If end year is a leap year, makes February 29 days then adds days
        else:
            daysOfMonths[1] == 29
            days += daysOfMonths[m]

    # Adds days from partial start month
    # Checks if start year is leap year
    if isLeapYear(y1) == False:
        # Subtracts start date from days of start month then adds to days
        days += daysOfMonths[m1] - d1
    else:
        # Changes February to 29 days if it is a leap year
        daysOfMonths[1] == 29
        # Subtracts start date from days of start month then adds to days
        days += daysOfMonths[m1] - d1

    # Adds days from partial end month
    days += d2

    return days

print daysBetweenDates(1986, 9, 10, 2016, 1, 13)
# Goal: 10,718