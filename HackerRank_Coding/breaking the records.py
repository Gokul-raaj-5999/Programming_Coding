#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max1=0
    min1=0
    c=scores[0]
    d=scores[0]
    for i in range (1,len(scores),1):
        if(scores[i]>scores[0] and scores[i]>c):
            c=scores[i]
            max1+=1
        elif(scores[i]<scores[0] and scores[i]<d):
            d=scores[i]
            min1+=1
    return(max1,min1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

##########################################################################
"""
SAMPLE1:
    INPUT:
        9
        10 5 20 20 4 5 2 25 1
    OUTPUT:
        2 4

SAMPLE2:
    INPUT:
        10
        3 4 21 36 10 28 35 5 24 42
    OUTPUT:
        4 0
"""
