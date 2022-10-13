#User function Template for python3
import math

class Solution:
    def countDivisibles (ob, A, B, M):
        c1 = math.floor(B//M)
        c2 = math.ceil(A//M)
        if c2*M < A:
            c2+= 1
        # print(c2, c1)
        if c2 == 0:
            c2 += 1
        if c2 < c1:
            # print(c1 - c2 + 1)
            return (c1 - c2 + 1)
        else:
            if c1:
                # print(1)
                return 1
            else:
                # print (0)
                return 0
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A, B, M = input().split()
        A = int(A)
        B = int(B)
        M = int(M)
        
        ob = Solution()
        print(ob.countDivisibles(A, B, M))
# } Driver Code Ends
