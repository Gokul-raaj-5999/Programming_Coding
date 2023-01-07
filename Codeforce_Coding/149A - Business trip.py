n = int(input())
arr = list(map(int, input().split()))
arr.sort( reverse= True)
sum = 0
i = 0
while sum < n and i < 12:
    sum += arr[i]
    i += 1
if sum >= n:
    print(i)
else:
    print('-1')