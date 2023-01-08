# Kadane's Algorithm

# Time Complexity: O(n)
# Space Complexity: O(1)

#if we have a array of +ve and -ve numbres then the sum of the elements 
#changes for element to element.. so in that case we have a totsum = X
# we have to find a sum that is >= totsum that is our aim
# sumfind(from subarray) >= total_sum.
# sys.maxsize value
# 32-bit: the value will be 2^31 – 1, i.e. 2147483647
# 64-bit: the value will be 2^63 – 1, i.e. 9223372036854775807


#best case - O(n)
arr = [-1,2,4,-3,5,2,-5,2]
n = len(arr)
best = 0
sum = 0
for a in range(0, n):
	sum = max(arr[a], sum+arr[a])
	best = max(best, sum)
print(best)


## average case - O(n^2)
# best = 0
# for a in range(0, n):
# 	sum = 0
# 	for b in range(a, n):
# 		sum += arr[b]
# 		best = max(best, sum)
# print(best)

## worst case - O(n^3)
# best = 0
# for a in range(0, n):
#     for b in range(a, n):
#         sum = 0
#         for k in range(a, b+1):
#             sum += arr[k]
#         best = max(best, sum)
# print(best)

