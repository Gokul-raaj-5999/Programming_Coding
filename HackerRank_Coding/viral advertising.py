#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    share=5
    like=0
    for i in range(0,n,1):
        lk=(share/2)
        like+=int(lk)
        share=int(lk)*3
    return like


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

###############################################################################
"""
SAMPLE1:
    INPUT:
        3
    OUTPUT:
        9

SAMPLE2:
    INPUT:
        4
    OUTPUT:
        15
"""
