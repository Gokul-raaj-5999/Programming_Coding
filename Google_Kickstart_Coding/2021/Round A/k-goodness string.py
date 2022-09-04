for x in range(1, int(input())+1):
    _ = list(map(int, input().split(" ")))
    n = _[0]
    k = _[1]
    s = str(input())
    count = 0
    for i in range(0,n//2):
        if(s[i]!=s[n-i-1]):
            count+=1
    if(count==k):
        print(f"Case #{x}: {0}")
    elif(count>k):
        print(f"Case #{x}: {count-k}")
    else:
        print(f"Case #{x}: {k-count}")
