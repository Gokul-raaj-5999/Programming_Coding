n = int(input())
for i in range(0, n):
	print(' '*(n-i), end = '')
	print(' '.join(map(str, str(11**i))))
