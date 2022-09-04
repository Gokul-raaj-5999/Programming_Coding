if __name__ == '__main__':
    inp=list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        inp.append([score,name])
inp.sort()
count=1
for j in range(1,len(inp),1):
    if(inp[j][0]!=inp[0][0]):break
    count+=1
for i in range(count,len(inp)):
    if(inp[i][0]!=inp[count][0]):break
    print(inp[i][1])

############################################################################
"""
INPUT:
    5
    Harry
    37.21
    Berry
    37.21
    Tina
    37.2
    Akriti
    41
    Harsh
    39

OUTPUT:
    Berry
    Harry
"""
