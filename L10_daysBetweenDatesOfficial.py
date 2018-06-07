# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
os.chdir('C:\Sources\IntroToCS')


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
        
    # YOUR CODE HERE!
    days = 0
    assert not isBefore(year2, month2, day2, year1, month1, day1)
    '''Throw AssertionError if False
    isBefore=True only if date1 < date2; False if date1 >= date2'''
    while True:
        if  year1 == year2 and month1 ==  month2 and day1 == day2:
            break
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    
    return days

def isBefore(year1, month1, day1, year2, month2, day2):
    '''The first date is earlier (not equal) than the second'''
    if year1 < year2:
        return True
    elif year1 == year2:
        if month1 < month2:
            return True
        elif month1 == month2:
            if day1 < day2:
                return True
    return False
        
def daysInMonth(year, month):
    listOfDays = [31,28,31,30,31,30,31,31,30,31,30,31]
    if isLeapYear(year) and month == 2:
        return 29
    return listOfDays[month-1]

def isLeapYear(year):
    if year%4 != 0:
        return False
    elif year%100 != 0:
        return True
    elif year%400 != 0:
        return False
    else:
        return True
#daysBetweenDates(2012,1,1,2012,1,3)
        
def test():
    assert daysBetweenDates(2013,1,1,2013,1,1) == 0
    assert daysBetweenDates(2013,1,1,2013,1,2) == 1
    assert daysBetweenDates(1900,2,28,1900,3,1) == 1
    assert daysBetweenDates(2012,2,28,2012,3,1) == 2
    assert daysBetweenDates(2012,3,1,2012,4,1) == 31
    print('Test finished!')