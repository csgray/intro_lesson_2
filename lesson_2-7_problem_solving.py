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
	
	return days

print daysBetweenDates(1986, 9, 10, 2016, 1, 13)
# Goal: 10,718