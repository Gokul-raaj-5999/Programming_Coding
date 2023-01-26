"""
Given a string, that contains a special character together with alphabets (‘a’ to ‘z’ and ‘A’ to ‘Z’), reverse the string in a way that special characters are not affected.

Examples: 
Input:   str = “a,b$c”
Output:  str = “c,b$a”

Explanation: Note that $ and , are not moved anywhere.  Only subsequence “abc” is reversed

Input:   str = “Ab,c,de!$”
Output:  str = “ed,c,bA!$”


time complexity  - O(n)
space complexity - O(n)
"""


s = input()
a = []
for i in s:
    a.append(i)
i,j = 0,len(s)-1

while i < j:
    if a[i].isalpha() and a[j].isalpha():
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1 
    elif a[i].isalpha() and a[j].isalpha()==False:
        j -= 1
    else:
        i += 1

op = ''.join( str(x) for x in a)
print(op)