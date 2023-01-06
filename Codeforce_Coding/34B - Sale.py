n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cost = 0

for i in range(0, m):
    if a[i] <= 0:
        cost = max(cost, cost+abs(a[i]))
print(cost)