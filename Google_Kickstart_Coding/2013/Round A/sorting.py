for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    alx, bob = [], []
    for i in arr:
        if(abs(i)%2!=0):
            alx.append(i)
        else:
            bob.append(i)
    alx.sort(reverse = True)
    bob.sort()
    ans = []
    for i in arr:
        if(i%2):
            ans.append(alx.pop())
        else:
            ans.append(bob.pop())
    s = ' '.join(map(str, ans))
    print(f"Case #{_+1}: {s}")
