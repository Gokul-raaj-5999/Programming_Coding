import collections

def solve():
    d = dict()
    d[1] = [1]
    n, f = map(int, input().split())
    for i in range(0, n-1):
        a, b = map(int, input().split())
        d[a]=d.get(a,[]) + [b]
        d[b]=d.get(b,[]) + [a]
    
    # print(d)
    vi=set()
    lans=[]
    q=collections.deque()
    q.append(1)
    while q:
        l=len(q)
        for i in range(l):
            a=q.popleft()
            vi.add(a)
            for j in d[a]:
                if j not in vi:
                    q.append(j)
        lans.append(l)
        
    ans=0
    aqe = []
    for i in range(0,f):
        aqe.append(int(input()))
    for i in lans:
        if i<=f:
            ans+=i
            f-=i
        else:
            break
    return ans


for t in range(0, int(input())):
    print(f"Case #{t+1}: {solve()}")
    
