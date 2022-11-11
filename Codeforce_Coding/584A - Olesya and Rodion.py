n , t = map(int, input().split())
if t == 10 and n == 1:
    print(-1)
elif t == 10:
    print(t*(10**(n-2)))
else:
    print(t*(10**(n-1))) 