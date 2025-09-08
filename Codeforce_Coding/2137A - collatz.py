import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    k, x = map(int, sys.stdin.readline().split())
    print(x * (1 << k))