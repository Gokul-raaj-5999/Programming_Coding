#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    dif=0
    sum1=0
    sum2 =0
    a=len(arr)
    for i in range (0,a,1):
       sum1 = sum1 + arr[i][i]
    for i in range (0,a,1):
       sum2 = sum2 + arr[i][a-1-i]
    if(sum1>sum2):
        dif = sum1 -sum2
    if(sum2>sum1):
        dif = sum2 -sum1
    return(dif)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

###########################################################################
"""
INPUT:
    3
    11 2 4
    4 5 6
    10 8 -12

OUTPUT:
    15
"""
