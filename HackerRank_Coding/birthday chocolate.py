#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below. s-choco   d-date (sum) m-month no of consecutive choco
def birthday(s, d, m):
    cnt = 0
    q = s[:m-1]
    for i in s[m-1:]:
        q.append(i)
        if (sum(q) == d):
            cnt += 1
        q.pop(0)
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

#############################################################################
"""
SAMPLE1:
    INPUT:
        5
        1 2 1 3 2
        3 2
    OUTPUT:
        2

SAMPLE2:
    INPUT:
        6
        1 1 1 1 1 1
        3 2
    OUTPUT:
        0

SAMPLE3:
    INPUT:
        1
        4
        4 1
    OUTPUT:
        1
"""
