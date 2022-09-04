#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the countTriplets function below.
def countTriplets(arr, r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in arr:
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1
    return(count)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

#########################################################################
"""
INPUT:
    4 2
    1 2 2 4
OUTPUT:
    2

INPUT:
    6 3
    1 3 9 9 27 81
OUTPUT:
    6

INPUT:
    5 5
    1 5 5 25 125
OUTPUT:
    4
"""
