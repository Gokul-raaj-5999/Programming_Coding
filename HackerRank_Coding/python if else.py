#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
a=n%2
if(a==0):
    if(2<=n<=5):
        print("Not Weird")
    elif(6<=n<=20):
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")

##############################################################################
"""
If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird

SAMPLE1:
    INPUT:
        3
    OUTPUT:
        Weird

SAMPLE2:
    INPUT:
        24
    OUTPUT:
        Not Weird
"""
