#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    max1=0
    for i in range(0,len(keyboards),1):
        if(keyboards[i]<b):
            for j in range(0,len(drives),1):
                if((keyboards[i]+drives[j])<=b and max1<keyboards[i]+drives[j]):
                    max1=keyboards[i]+drives[j]
    if(max1>0):
        return max1
    else:
        return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    """The maximum amount of money she can spend on a keyboard and USB drive,
    or -1 if she can't purchase both items"""
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()

##############################################################################
"""
SAMPLE1:
    INPUT:
        10 2 3
        3 1
        5 2 8
    OUTPUT:
        9

SAMPLE2:
    INPUT:
        5 1 1
        4
        5
    OUTPUT:
        -1
"""
