#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    for i in range(1,10000,1):
        n1=(x1+(i*v1))
        n2=(x2+(i*v2))
        if(n1==n2):
            if (x1>x2 and v1<v2 ):
                return "YES"
            elif(x2>x1 and v2<v1):
                return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

###############################################################################
"""
SAMPLE1:
    INPUT:
        0 3 4 2
    OUTPUT:
        YES

SAMPLE2:
    INPUT:
        0 2 5 3
    OUTPUT:
        NO
"""
