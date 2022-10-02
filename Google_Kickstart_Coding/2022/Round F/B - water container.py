import collections
d = dict()
d[1] = [1]

def add_adj(a,b):
    d[a]=d.get(a,[]) + [b]
    d[b]=d.get(b,[]) + [a]


def findNodes_in_lev():
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
    return lans

if __name__ == '__main__':
    t = int(input())
    for t in range(0, t):
        n, f = map(int, input().split())
        for i in range(0, n-1):
            a, b = map(int, input().split())
            add_adj(a,b)
        
        # print(d)

        lans = findNodes_in_lev()
        # print('nodes in each level',lans)
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
        print(f"Case #{t+1}: {ans}")
    
