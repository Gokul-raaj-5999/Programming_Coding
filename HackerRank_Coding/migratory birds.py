#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr,arr_count):
    bird = [0, 0, 0, 0, 0, 0]
    for i in range(len(arr)):
        bird[arr[i]] += 1
    return bird.index(max(bird))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr,arr_count)

    fptr.write(str(result) + '\n')

    fptr.close()

############################################################################
"""
SAMPLE1:
    INPUT:
        6
        1 4 4 4 5 3
    OUTPUT:
        4

SAMPLE2:
    INPUT:
        11
        1 2 3 4 5 4 3 2 1 3 4
    OUTPUT:
        3
"""
