#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count=0
    num2=0
    for i in range(0,n,1):
        if(s[i]=="U"):
            count+=1
            if(count==0 ):
                num2+=1
        else:
            count-=1
    return num2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

###########################################################################
"""
SAMPLE1:
    INPUT:
        8
        UDDDUDUU
    OUTPUT:
        1

SAMPLE2:
    INPUT:
        12
        DDUUDDUDUUUD
    OUTPUT:
        2
"""
