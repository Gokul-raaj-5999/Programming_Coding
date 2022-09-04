#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    c=0
    for i in a:
        if(i<=0):
            c+=1
    if(c<k):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()

#############################################################################
"""
INPUT:
    2
    4 3
    -1 -3 4 2
    4 2
    0 -1 2 1
OUTPUT:
    YES
    NO
"""
