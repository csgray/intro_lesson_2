# Lesson 2.7: How to Solve Problems - Days Between Dates

# In this lesson, you'll be working on solving a much
# bigger problem than those you've seen so far. If you
# want, you can use this starter code to write your
# quiz responses and then copy and paste into the
# Udacity quiz nodes.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4184188665/m-108325398

# Simple Mechanical Algorithm
# days = 0
# while date1 is before date2:
#     date1 = advance to next day
#     days += 1

# Fill in the functions below to solve the problem.

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

def daysInMonth(year, month):
    # Checks if the month is one of the ones with 31 days
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    # Checks if the month is February
    if month == 2:
        if isLeapYear(year) == True:
            return 29
        else:
            return 28
    else:
        return 30

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

# Below is a testing script that will check if your code is doing
# what it is supposed to. Don't change it! The test will run
# when you execute the file.
# Bonus: Can you figure out how the test works?

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
            print result
        else:
            print "Test case passed!"

test()

###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###
#
#def nextDay(year, month, day):
#    """
#    Returns the year, month, day of the next day.
#    Simple version: assume every month has 30 days.
#    """
#    if day < 30:
#        return year, month, day + 1
#    elif day == 30:
#        if month < 12:
#            return year, month + 1, 1
#        if month == 12:
#            return year + 1, 1, 1

# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 
#
#def nextDay(year, month, day):
#    """Simple version: assume every month has 30 days"""
#    if day < 30:
#        return year, month, day + 1
#    else:
#        if month == 12:
#            return year + 1, 1, 1
#        else:
#            return year, month + 1, 1
#
#def dateIsBefore(year1, month1, day1, year2, month2, day2):
#    if year1 < year2:
#        return True
#    elif month1 < month2:
#        return True
#    elif day1 < day2:
#        return True
#    else:
#        return False
#        
#def daysBetweenDates(year1, month1, day1, year2, month2, day2):
#    """Returns the number of days between year1/month1/day1
#       and year2/month2/day2. Assumes inputs are valid dates
#       in Gregorian calendar, and the first date is not after
#       the second."""
#    days = 0
#    while dateIsBefore(year1, month1, day1, year2, month2, day2) == True:
#        nextDay(year1, month1, day1)
#        days +=1
#        year1, month1, day1 = nextDay(year1, month1, day1)
#    return days
#
#def test():
#    test_cases = [((2012,9,30,2012,10,30),30), 
#                  ((2012,1,1,2013,1,1),360),
#                  ((2012,9,1,2012,9,4),3)]
#    
#    for (args, answer) in test_cases:
#        result = daysBetweenDates(*args)
#        if result != answer:
#            print "Test with data:", args, "failed"
#            print result
#        else:
#            print "Test case passed!"
#
#test()

# Instructor Assert
# assert not dateIsBefore(year2, month2, day2, year1, month1, day1)

