# this is binary search and printing its worst case effiency that is we search for the last element and the number of 
#itereation that is required to search that element is given by count.. but in upper bound of mid element 

import math

def search(a, x): # gives its index
    s = 0
    e = len(a)
    if x > a[-1] or x < a[0]:
        return -1
    while s <= e:
        mid = (s+e)//2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            e = mid -1
        elif a[mid] < x:
            s = mid +1
    return -1


def bsec(a , x):   # gives position 
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
