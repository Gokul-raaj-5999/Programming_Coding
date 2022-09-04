#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    for i in s1:
        if(i in s2):
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

#############################################################################
"""
SAMPLE1:
    INPUT:
        2
        hello
        world
        hi
        world
    OUTPUT:
        YES
        NO

SAMPLE2:
    INPUT:
        4
        wouldyoulikefries
        abcabcabcabcabcabc
        hackerrankcommunity
        cdecdecdecde
        jackandjill
        wentupthehill
        writetoyourparents
        fghmqzldbc
    OUTPUT:
        NO
        YES
        YES
        NO

SAMPLE3:
    INPUT:
        2
        aardvark
        apple
        beetroot
        sandals
    OUTPUT:
        YES
        NO
"""
