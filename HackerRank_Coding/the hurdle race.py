#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    height.sort(reverse=True)
    if(k>height[0]):
        return 0
    else:
        return height[0]-k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()

############################################################################
"""
SAMPLE1:
    INPUT:
        5 4
        1 6 3 5 2
    OUTPUT:
        2

SAMPLE2:
    INPUT:
        5 7
        2 5 4 5 2
    OUTPUT:
        0
"""
