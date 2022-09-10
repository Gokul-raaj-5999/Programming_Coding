def zfunction1(string): # time complexity O(m+n)
    n = len(string)
    z = [0]*n
    l, r, k = 0, 0, 0
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and string[r - l] == string[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and string[r - l] == string[r]:
                    r += 1
                z[i] = r - l
                r -= 1
    return z


def zfunction2(string): # time complexity O(n^2)
    n = len(string)
    z = [0]*n
    for i in range(1, n):
        while (i + z[i] < n and string[z[i]] == string[i+ z[i]] ):
            z[i] += 1
    return z


s = 'abacaba'
print(zfunction1(s))
print(zfunction2(s))

"""
Z-function and its calculation
Suppose we are given a string  of length . The Z-function for this string is an array of length  where the -th element is equal to the greatest number of characters starting from the position  that coincide with the first characters of .

In other words,  is the length of the longest string that is, at the same time, a prefix of  and a prefix of the suffix of  starting at .

Note. In this article, to avoid ambiguity, we assume -based indexes; that is: the first character of  has index  and the last one has index .

The first element of Z-function, , is generally not well defined. In this article we will assume it is zero (although it doesn't change anything in the algorithm implementation).

This article presents an algorithm for calculating the Z-function in  time, as well as various of its applications.

Examples
For example, here are the values of the Z-function computed for different strings:

"aaaaa" - [0, 4, 3, 2, 1]
"aaabaab" - [0, 2, 1, 0, 2, 1, 0]
"abacaba" - [0, 0, 1, 0, 3, 0, 1]
"""