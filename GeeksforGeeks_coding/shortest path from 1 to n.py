#User function Template for python3

class Solution:
    def minStep (self, n):
        #complete the function here
        tem = n
        c = 0
        while tem > 1:
            if tem%3 == 0:
                tem //= 3
                c += 1
            elif tem%3 != 0:
                tem -= 1
                c += 1
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        print(ob.minStep(n))
# } Driver Code Ends
