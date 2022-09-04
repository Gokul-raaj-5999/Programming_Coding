#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if (s[-2:] == "AM" and s[:2] == "12"):
        return "00" + s[2:-2]
    elif (s[-2:] == "AM"):
        return s[:-2]
    elif (s[-2:] == "PM" and s[:2] == "12"):
        return s[:-2]
    else:
        return str(int(s[:2]) + 12) + s[2:8]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

##########################################################################
"""
INPUT:
    07:05:45PM

OUTPUT:
    19:05:45
"""
