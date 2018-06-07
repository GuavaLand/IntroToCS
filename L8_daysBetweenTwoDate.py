# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 09:49:05 2018

@author: yyuan1
"""

import os

os.chdir('C:\Sources\IntroToCS')

   
daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysOfMonths_leap = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = daysOfYears(year1, month1, day1, year2, month2, day2) +\
            daysOfMon(year1, month1, day1, year2, month2, day2) +\
             daysOfDays(year1, month1, day1, year2, month2, day2)
    return days 
    
def daysOfYears(year1, month1, day1, year2, month2, day2): #days of years in between
    ydays = 0
    if year2 > year1:
        for i in range(year1 + 1, year2):
            if isLeap(i):
                ydays += 366
            else:
                ydays += 365
    return ydays
  
def daysOfMon(year1, month1, day1, year2, month2, day2): #days of months in between
    mdays = 0
    if year2 > year1:
        for i in range(month1 + 1, 13):
            if isLeap(year1):
                mdays += daysOfMonths_leap[i-1]
            else:
                mdays += daysOfMonths[i-1]
        for i in range(1, month2):
            if isLeap(year2):
                mdays += daysOfMonths_leap[i-1]
            else:
                mdays += daysOfMonths[i-1]
    else: #same year
        if month2 > month1:
            for i in range(month1 + 1, month2):
                if isLeap(year1):
                    mdays += daysOfMonths_leap[i-1]
                else:
                    mdays += daysOfMonths[i-1]
    return mdays
        
def daysOfDays(year1, month1, day1, year2, month2, day2):
    ddays = 0
    if isLeap(year1):
        ddays1 = daysOfMonths_leap[month1-1] - day1
    else:
        ddays1 = daysOfMonths[month1-1] - day1
    ddays2 = day2
    ddays = ddays1 + ddays2
    return ddays


def isLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")

test()
