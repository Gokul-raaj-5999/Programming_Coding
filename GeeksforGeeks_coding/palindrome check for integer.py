#User function Template for python3

class Solution:
	def is_palindrome(self, n):
	    if str(n) == str(n)[::-1]:
	        return 'Yes'
	    else:
	        return 'No'
		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_palindrome(n)
		print(ans)
# } Driver Code Ends
