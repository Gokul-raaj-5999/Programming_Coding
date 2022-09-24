#if we have a array of +ve and -ve numbres then the sum of the elements 
#changes for element to element.. so in that case we have a totsum = X
# we have to find a sum that is >= totsum that is our aim
# sumfind(from subarray) >= total_sum.

maxint = 99999999999

def maxSubArraySum(a, size):

	totsum = -maxint - 1
	subsum = 0

	for i in range(0, size):
		totsum += a[i]
		if (subsum < totsum):
			subsum = totsum

		if totsum < 0:
			totsum = 0

	return subsum

a = [-2, -3, 4, -1, -2, 1, 5, -3]

print (f"total sum = {sum(a)}, max sum of subarray = {maxSubArraySum(a, len(a))}" )
