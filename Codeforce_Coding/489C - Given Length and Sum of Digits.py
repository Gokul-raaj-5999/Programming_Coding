n, s = map(int, input().split())
if n==1 and s==0:
    print('0 0')
elif (9*n) < s or s == 0:
    print('-1 -1')
else:
    k = 10**(n-1)
    for i in range(s-1):
        k += 10**(i//9)
    k2 = 0
    for i in range(s):
        k2 += 10**(n-1-i//9)
    print(k, k2)
