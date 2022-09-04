"""
Marie invented a Time Machine and wants to test it by time-traveling to visit
Russia on the Day of the Programmer (the 256th day of the year) during a year in the
inclusive range from 1700 to 2700.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if (year == 1918):
        return '26.09.1918'
    elif ((year <= 1917) & (year%4 == 0)) or ((year > 1918) & (year%400 == 0 or
     ((year%4 == 0) & (year%100 != 0)))):
        return '12.09.%s' %year
    else:
        return '13.09.%s' %year

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

################################################################################
"""
SAMPLE1:
    INPUT:
        2017
    OUTPUT:
        13.09.2017

SAMPLE2:
    INPUT:
        2016
    OUTPUT:
        12.09.2016

SAMPLE3:
    INPUT:
        1800
    OUTPUT:
        12.09.1800
"""
