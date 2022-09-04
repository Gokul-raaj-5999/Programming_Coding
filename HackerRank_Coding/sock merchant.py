#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    ar.sort()
    ar.append('#')
    i = 0
    while i<n:
        if ar[i]==ar[i+1]:
            count+=1
            i+=2
        else:
            i+=1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

#############################################################################
"""
SAMPLE1:
    INPUT:
        9
        10 20 20 10 10 30 50 10 20
    OUTPUT:
        3

SAMPLE2:
        INPUT:
            10
            1 1 3 1 2 1 3 3 3 3
        OUTPUT:
            4
"""
