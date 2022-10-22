"""
Approach 3: Sliding Window Optimized
Intuition
The above solution requires at most 2n steps. In fact, it could be optimized to require only n steps. Instead of 
using a set to tell if a character exists or not, we could define a mapping of the characters to its index. Then we can
 skip the characters immediately when we found a repeated character.

Algorithm
The reason is that if s[j]s[j] have a duplicate in the range [i, j)[i,j) with index j'j ′ 
, we don't need to increase ii little by little. We can skip all the elements in the range [i, j'][i,j] 
and let ii to be j' + 1j +1 directly.

Complexity Analysis
Time complexity : O(n)
O(n). Index jj will iterate nn times.
Space complexity : O(min(m, n))
O(min(m,n)). Same as the previous approach.
"""

def findmaxlenofSsting(s):
    n = len(s)
    ans = 0
    # mp stores the current index of a character
    mp = {}

    i = 0
    # try to extend the range [i, j]
    for j in range(n):
        if s[j] in mp:
            i = max(mp[s[j]], i)

        ans = max(ans, j - i + 1)
        mp[s[j]] = j + 1

    return ans

for i in range(0, int(input())):
    print( findmaxlenofSsting(input()))