#User function template for Python

class Solution:	
	def remove_duplicate(self, A, N):
		# code here
		count = N
		i = 0
		j = 1
		while j < N:
		    if A[i] == A[j]:
		        j += 1
		    else:
		        i += 1
		        A[i] = A[j]
		        
		return i+1


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends
