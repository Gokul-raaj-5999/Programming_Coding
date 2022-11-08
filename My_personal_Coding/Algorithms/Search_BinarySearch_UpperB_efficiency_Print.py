# this is binary search and printing its worst case effiency that is we search for the last element and the number of 
#itereation that is required to search that element is given by count.. but in upper bound of mid element 

import math

def bsec(a , x):
    start = 0
    end = len(a)
    
    count = 1
    while start < end:
        mid = (start + end)//2  #binary search in upper bound on mid 
        if a[mid] == x:
            return count
        elif a[mid] < x:
            start = mid
        elif a[mid] > x:
            end = mid
        count += 1
        print(a[mid])
    return count
       

def solve():
    n = int(input())
    arr = []
    for i in range(0, n):
        arr.append(i+1)
    print(arr)

    count = bsec(arr, n)
    return count


for t in range(0, int(input())):
    ans = solve()
    print(t+1, "-", ans)
