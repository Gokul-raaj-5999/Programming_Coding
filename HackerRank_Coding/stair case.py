#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    i=1
    while(i<n):
        print((n-1-i)*" ",(i)*"#")
        i=i+1
    if(i==n):
        print(i*"#")

if __name__ == '__main__':
    n = int(input())

    staircase(n)

############################################################################
"""
INPUT:
    6
OUTPUT:
         #
        ##
       ###
      ####
     #####
    ######
"""
