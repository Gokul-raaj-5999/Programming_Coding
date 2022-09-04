#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    tp=0
    count=dict()
    for i in arr:
        count[i]=count.get(i,i)
    #print(sorted(count.keys()))
    for j in arr:
        print(count[j],count.get(j+k,-1))
        if(count[j]-count.get(j+k,0)==k or count.get(j+k,0)-count[j]==k):
            #print("loop",count[j],count.get(j+k,0))
            tp+=1
            #print(arr[j],arr[j]+2)
    return tp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

############################################################################
"""
SAMPLE1:
        INPUT:
                5 2
                1 5 3 4 2
        OUTPUT:
                3
SAMPLE2:
        INPUT:
                10 1
                363374326 364147530 61825163 1073065718 1281246024 1399469912 428047635 491595254 879792181 1069262793
        OUTPUT:
                0
SAMPLE3:
        INPUT:
                7 2
                1 3 5 8 6 4 2
        OUTPUT:
                5
"""
