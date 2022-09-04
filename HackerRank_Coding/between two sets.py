#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    ct=0
    for i in range(max(a),min(b)+1):
        for j in a:
            if i%j!=0:
                break
        else:
            for k in b:
                if k%i!=0:
                    break
            else:
                ct+=1
    return ct


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

##############################################################################
"""
SAMPLE1:
    INPUT:
        2 3
        2 4
        16 32 96
    OUTPUT:
        3

SAMPLE2:
    INPUT:
        2 2
        3 4
        24 48
    OUTPUT:
        2
"""
