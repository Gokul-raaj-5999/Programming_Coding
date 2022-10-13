#User function Template for python3

class Solution:
    def canJump(self, N):
        # code here 
        if (N&(N-1))==0:
            return "True"
        else:
            return "False"


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.canJump(N))
# } Driver Code Ends
