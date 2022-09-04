room = 0
for i in range(int(input())):
    p,q = map(int, input().split())
    if(p < q and q-p>=2 ):
        room+=1
print(room)