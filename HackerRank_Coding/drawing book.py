#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    num1=0
    num2=0
    if(p==1 or p==n):
        return 0
    if(p%2==0):
        num1=int(p/2)
        num2=int((n-p)/2)
    else:
        num1=int((p-1)/2)
        num2=int((n-(p-1))/2)
    if(num1<num2):
        return num1
    else:
        return num2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

#############################################################################
"""
SAMPLE1:
    INPUT:
        6
        2
    OUTPUT:
        1

SAMPLE2:
    INPUT:
        5
        4
    OUTPUT:
        0
"""
