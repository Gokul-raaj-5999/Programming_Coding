n = int(input())
val = list(map(int, input().split()))
nex = []
dis = {}
for i in val:
    if i in dis:
        dis[i] += 1
    else:
        dis[i] = 1
# print(dis)
val.sort(reverse=True)
while(sum(val) >= sum(nex)):
    # print(val,nex)
    nex.append(val.pop(0))
# print(val,nex)
print(len(nex))