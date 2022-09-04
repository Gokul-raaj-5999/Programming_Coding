#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    ad=m%n
    if(m==n or ad==0):
        out=s+n-1
        if(out>n):
            out=out-n
        return(out)
    out=s+ad-1
    if(out>n):
        out=out-n
    return out


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()

###############################################################################
"""
SAMPLE1:
    INPUT:
        2
        5 2 1
        5 2 2
    OUTPUT:
        2
        3

SAMPLE2:
    INPUT:
        2
        7 19 2
        3 7 3
    OUTPUT:
        6
        3
"""
