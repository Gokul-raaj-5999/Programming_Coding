#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    count=0
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()

###############################################################################
"""
SAMPLE1:
    INPUT:
        5
        AAAA
        BBBBB
        ABABABAB
        BABABA
        AAABBB
    OUTPUT:
        3
        4
        0
        0
        4

SAMPLE2:
    INPUT:
        3
        AAABBBAABB
        AABBAABB
        ABABABAA
    OUTPUT:
        6
        4
        1

SAMPLE3:
    INPUT:
        1
        ABBABBAA
    OUTPUT:
        3
"""
