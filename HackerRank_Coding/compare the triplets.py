#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    sum1=0
    sum2=0
    for i in range (len(a)):
        if(a[i]>b[i]):
            sum1+=1
        if(a[i]<b[i]):
            sum2+=1
    return (sum1,sum2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

##########################################################################
"""
SAMPLE1:
    INPUT:
        5 6 7
        3 6 10
    OUTPUT:
        1 1

SAMPLE2:
    INPUT:
        17 28 30
        99 16 8
    OUTPUT:
        2 1
"""
