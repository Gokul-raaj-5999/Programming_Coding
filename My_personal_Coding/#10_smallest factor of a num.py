# Function to find the smallest divisor for a number.
def smallestDivisor(n):
	if (n % 2 == 0):
		return 2
	i = 3
	while(i * i <= n):
		if (n % i == 0):
			return i
		i += 2

	return n


n = 31
print(smallestDivisor(n))