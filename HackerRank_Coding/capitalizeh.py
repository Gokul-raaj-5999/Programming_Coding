#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    space=re.findall('(\s+)',s)
    print(space)
    s=s.split()
    print(s)
    outp=''
    count=0
    j=0
    for i in s:
        outp+=str(i.capitalize())
        count+=1
        if(count<len(s)):
            outp+=space[j]
            j+=1
    return outp.rstrip()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

############################################################################
"""
INPUT:
      hello world

OUTPUT:
      Hello World
"""
