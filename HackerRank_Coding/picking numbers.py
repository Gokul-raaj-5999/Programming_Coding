#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    diff=0
    a1=0
    b=[]
    a.sort()
    if(a[0]==a[len(a)-1]):
        return len(a)
    for i in range(0,len(a),1):
        for j in range (i+1,len(a),1):
            if(a[i]==a[j] or a[j]-1==a[i]):
                a1+=1
            else:
                a1+=1
                b.append(a1)
                a1=0
                break
    if(a1+1==len(a)):
        return len(a)
    b.sort(reverse=True)
    return b[0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

###############################################################################
"""
SAMPLE1:
    INPUT:
        6
        4 6 5 3 3 1
    OUTPUT:
        3

SAMPLE2:
    INPUT:
        6
        1 2 2 3 1 2
    OUTPUT:
        5
"""
