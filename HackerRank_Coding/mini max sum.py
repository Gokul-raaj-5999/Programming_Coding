#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    min1=0
    max1=0
    for i in range (0,4,1):
        min1+=arr[i]
        max1+=arr[i+1]
    print(min1,max1)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

########################################################################
"""
SAMPLE1:
    INPUT:
        1 2 3 4 5
    OUTPUT:
        10 14

SAMPLE2:
    INPUT:
        7 69 2 221 8974
    OUTPUT:
        299 9271
"""
