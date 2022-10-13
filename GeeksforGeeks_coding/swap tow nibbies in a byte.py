#User function Template for python3
class Solution:
    def swapNibbles (self, n):
        # code here
        left = n&15
        left = left <<4
        right = n>>4
        return left|right
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.swapNibbles(N))
# } Driver Code Ends
