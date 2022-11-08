t = int(input())
 
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print("Yes" if arr[0] == min(arr) else "No")