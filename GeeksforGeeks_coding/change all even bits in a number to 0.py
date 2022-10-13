#User function Template for python3
class Solution:
    def convertEvenBitToZero (ob, n):
        # code here 
        s = str(bin(n)[2:].split())
        s = s[2:-2][::-1]
        op = ''
        for i in range(0, len(s)):
            # print(s[i])
            if i%2 == 0 and s[i] == '1':
                op+='0'
            else:
                op+= s[i]
                
        op = op[::-1]
        # print(op)
        ans = int(op, 2)
        return ans
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.convertEvenBitToZero(n))
# } Driver Code Ends
