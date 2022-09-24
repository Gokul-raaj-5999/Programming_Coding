#if we have a array of +ve and -ve numbres then the sum of the elements 
#changes for element to element.. so in that case we have a totsum = X
# we have to find a sum that is >= totsum that is our aim
# sumfind(from subarray) >= total_sum.
from sys import maxsize

def maxSubArraySum(a, size):
	maxsum = 0
	cursum = 0
	maxval = -maxsize -1
	minval = maxsize

	for x in a:
		maxval = max(maxval, x)
		minval = min(minval, x)
	
	if maxval <= 0: # will have max as neg val so have to print -ve maxval  in this case.
		return maxval #u can return minval or int 0 its ur choice
	
	for i in range(0, size):  # this loop goes for +ve maxval
		cursum += a[i]
		maxsum = max(maxsum, cursum)
		if cursum < 0:
			cursum = 0
		
	return maxsum	

a = [-1, 0, -3, 0]

print (f"total sum = {sum(a)}, max sum of subarray = {maxSubArraySum(a, len(a))}" )
