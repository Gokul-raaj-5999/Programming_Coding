#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count1=0
    count2=0
    for i in range (0,len(apples),1):
        if ((apples[i]+a)>=s and (apples[i]+a)<=t):
            count1+=1
    for j in range (0,len(oranges),1):
        if ((oranges[j]+b)>=s and (oranges[j]+b)<=t):
            count2+=1
    print(count1)
    print(count2)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

#############################################################################
"""
Input Format:
The first line contains two space-separated integers denoting the respective values of  s and t.
The second line contains two space-separated integers denoting the respective values of a and b.
The third line contains two space-separated integers denoting the respective values of m and n.
The fourth line contains m space-separated integers denoting the respective distances that each apple falls from point a .
The fifth line contains n space-separated integers denoting the respective distances that each orange falls from point b.

Output Format:
Print two integers on two different lines:
The first integer: the number of apples that fall on Sam's house.
The second integer: the number of oranges that fall on Sam's house.

INPUT:
    7 11
    5 15
    3 2
    -2 2 1
    5 -6
OUTPUT:
    1
    1
"""
