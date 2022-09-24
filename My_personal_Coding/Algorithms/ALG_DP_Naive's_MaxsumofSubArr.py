# Naive Approach

# Time Complexity: O(n3)
# Space Complexity: O(1)

#if we have a array of +ve and -ve numbres then the sum of the elements 
#changes for element to element.. so in that case we have a totsum = X
# we have to find a sum that is >= totsum that is our aim
# sumfind(from subarray) >= total_sum.
# sys.maxsize value
# 32-bit: the value will be 2^31 – 1, i.e. 2147483647
# 64-bit: the value will be 2^63 – 1, i.e. 9223372036854775807

from sys import maxsize

def maxSubArraySum(a, size):
    maxsum = -maxsize - 1

    for i in range(0, size):
        for j in range(0, size):
            cursum = 0
            for k in range(i, j+1):
                cursum += a[k]
            maxsum = max(maxsum, cursum)
            
    return maxsum

a = [-1, 0, -3, 0]

print (f"total sum = {sum(a)}, max sum of subarray = {maxSubArraySum(a, len(a))}" )
