#User function Template for python3

class Solution:
    def sortedCount(self,N,M,Mat):
        def call(lst):
            i = 0
            a = 0
            b = 0
            while i < len(lst)-1:
                if a == 0 and b == 0:
                    if lst[i] < lst[i+1]:
                        a = 1
                        b = 0
                    elif lst[i] > lst[i+1]:
                        a = 0
                        b = 1
                    else:
                        return 0
                elif a == 1:
                    if lst[i] > lst[i+1] or lst[i] == lst[i+1]:
                        return 0
                    else:
                        i += 1
                elif b ==1:
                    if lst[i] < lst[i+1] or lst[i] == lst[i+1]:
                        return 0
                    else:
                        i += 1
                
            return 1
            
        count =0 
        for lst in Mat:
            if call(lst):
                count += 1
            
        return (count)
             

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        Mat=[]
        for i in range(N):
            Mat.append(list(map(int,input().strip().split(" "))))
        ob=Solution()
        ans=ob.sortedCount(N,M,Mat)
        print(ans) 
# } Driver Code Ends
