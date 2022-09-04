#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    h=0
    for i in range(0,n+1,1):
        if(i==0 or (i%2)==0):
            h+=1
        else:
            h*=2
    return h

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()

###############################################################################
"""
SAMPLE1:
    INPUT:
        2
        0
        1
    OUTPUT:
        1
        2

SAMPLE2:
    INPUT:
        2
        4
        3
    OUTPUT:
        7
        6
"""
