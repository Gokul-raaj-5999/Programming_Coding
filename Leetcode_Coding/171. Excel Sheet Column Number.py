class Solution:
    def titleToNumber(self, s: str) -> int:
        l = len(s)
        a = []
        for i in range(0, l):
            a.append(s[i])
            
        a.reverse()
        print(a)
        sum = 0
        for i in range(0, l):
            x = (26**(i)) * (ord(a[i])-64)
            print(x , 26**(i), ord(a[i])-64)
            sum += x
            print(sum)
            
        return sum
            
            

"""
171. Excel Sheet Column Number
Easy

3707

299

Add to List

Share
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
 

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
"""
