#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    sum1=0
    avg=0
    for i in range (0,len(bill),1):
        if(i!=k):
            sum1+=bill[i]
    avg = int (sum1/2)
    if(b==avg):
        print("Bon Appetit")
    else:
        c=b-avg
        print(c)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

#########################################################################
"""
SAMPLE1:
    INPUT:
        4 1
        3 10 2 9
        12
    OUTPUT:
        5

SAMPLE2:
    INPUT:
        4 1
        3 10 2 9
        7
    OUTPUT:
        Bon Appetit
"""
