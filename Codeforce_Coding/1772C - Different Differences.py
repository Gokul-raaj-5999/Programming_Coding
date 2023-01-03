for _ in range(int(input())):
    k,n=map(int,input().split())
    for i in range(k):
        print(min(1+(i*(i+1))//2,n-k+i+1),end=' ')
    print()