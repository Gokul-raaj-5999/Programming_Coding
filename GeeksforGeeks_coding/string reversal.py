#eleminate all the duplicate elements and space.
#User function Template for python3

class Solution:
    def reverseString(self, s):
        # code here
        lst = [0]*26
        
        s = s[::-1]
        op = ''
        for ele in s:
            if ele == ' ':
                continue
            ind = ord(ele) - 65
            # print(ind)
            if lst[ind] == 0:
                op += ele
                lst[ind] = 1

        return op
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        
        ob = Solution()
        ans = ob.reverseString(s)
        print(ans)
# } Driver Code Ends
