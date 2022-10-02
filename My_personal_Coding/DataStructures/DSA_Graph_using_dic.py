import collections
d = dict()

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
    n = int(input())
    for i in range(0, n):
        a, b = map(int, input().split())
        add_adj(a,b)
    
    print(d)

    lans = findNodes_in_lev()
    print('nodes in each level',lans)
    