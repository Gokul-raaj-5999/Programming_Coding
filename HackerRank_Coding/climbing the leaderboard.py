#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)))
    index = 0
    rank_list = []
    n = len(scores)
    for i in alice:
        while (n > index and i >= scores[index]):
            index += 1
        rank_list.append(n+1-index)
    return rank_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

##############################################################################
"""
SAMPLE1:
    INPUT:
        7
        100 100 50 40 40 20 10
        4
        5 25 50 120
    OUTPUT:
        6
        4
        2
        1

SAMPLE2:
    INPUT:
        6
        100 90 90 80 75 60
        5
        50 65 77 90 102
    OUTPUT:
        6
        5
        4
        2
        1
"""
