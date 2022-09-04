for t in range (int(input())):
    n,x,y = list(map(int, input().split()))
    tot = (n*(n+1))//2
    if(tot%(x+y)!=0 ):
        print(f'Case #{t+1}: IMPOSSIBLE')
    else:
        print(f'Case #{t+1}: POSSIBLE')
        sum = x*(tot//(x+y))
        vec = []
        for i in range(n,0,-1):
            if(i<=sum):
                vec.append(i)
                sum-=i
        print(len(vec))
        for x in vec:
            print(x, end= " ")
        print()
