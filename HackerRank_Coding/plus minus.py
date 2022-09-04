#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    l1=len(arr)
    pos=0
    neg=0
    zer=0
    p1=0
    n1=0
    z1=0
    for i in arr:
        if(i>0):
            pos+=1
        elif(i<0):
            neg+=1
        elif(i==0):
            zer+=1
    p1=(pos/l1)
    n1=(neg/l1)
    z1=(zer/l1)
    num1=[p1,n1,z1]
    return (num1)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result=plusMinus(arr)
    for i in result:
        print(i)

###################################################################
"""
SAMPLE1:
    INPUT:
        6
        -4 3 -9 0 4 1
    OUTPUT:
        0.500000
        0.333333
        0.166667

SAMPLE2:
    INPUT:
        8
        1 2 3 -1 -2 -3 0 0
    OUTPUT:
        0.375000
        0.375000
        0.250000
"""
