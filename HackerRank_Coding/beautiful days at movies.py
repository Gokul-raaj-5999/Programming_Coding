#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count=0
    for a in range (i,j+1,1):
        rev=0
        nv=a
        while(nv>0):
            per=nv%10
            rev=rev*10+per
            nv=int((nv-per)/10)
        be=abs(a-rev)
        res=be/k
        if(res==int(res)):
            count+=1
    return(count)
        #print(a)
#221->122 \\ 221%10=1 rev=1 nv=22 \\ 22%10=2 rev=12 nv=2 \\ 2%10=2 rev=122 nv=0
#rev=0 nv=221 \\per=nv%10 rev=rev*10+per nv/=10

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()

##############################################################################
"""
SAMPLE1:
    INPUT:
        20 23 6
    OUTPUT:
        2

SAMPLE2:
    INPUT:
        13 45 3
    OUTPUT:
        33
"""
