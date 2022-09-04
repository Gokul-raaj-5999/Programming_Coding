class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''
        disc = {}
        min = 999999999999999
        for i in range(0,len(strs)):
            disc[i] = len(strs[i])
            if(len(strs[i]) < min):
                min = len(strs[i])
        print(disc, min)
        i = 0
        if(len(strs)==1):
            return(strs[0])
                   
        while(i<min):
            ind = 0
            flag = 1
            while(ind < len(strs)-1 and flag == 1):
                if(strs[ind][i] == strs[ind+1][i]):
                    flag = 1
                    ind+=1
                else:
                    flag = 0
                    break
            if(flag == 1):
                s+= strs[0][i]
            else:
                break
            i+=1
        print(s)
        return(s)
        
        
        
"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
