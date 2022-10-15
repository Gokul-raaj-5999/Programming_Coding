#done 

def solve():
    p, d, my = list(map(int, input().split()))

    par = []
    for i in range(0, p):
        x = list(map(int, input().split()))
        if i == my-1:
            myarr = x
        par.append(x)
    # print(par)
    
    new = []
    for i in range(0, len(par[0])):
        x = []
        for j in range(0, len(par)):
            x.append(par[j][i])
        new.append(x)
    # print(new)
    count = 0 
    for i in range(0, len(myarr)):
        m = max(new[i])
        if myarr[i] < m:
            count += m - myarr[i]
    
    return count 



for t in range(0, int(input())):
    print(f'Case #{t+1}: {solve()}')