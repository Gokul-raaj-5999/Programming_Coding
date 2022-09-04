for x in range (0,int(input())):
    n = int(input())
    p = str(input())
    r = [0]*n
    b = [0]*n
    y = [0]*n
    for i in range(0,n):
        if(p[i]=='R'):
            r[i]=1
        elif(p[i]=='Y'):
            y[i]=1
        elif(p[i]=='B'):
            b[i]=1
        elif(p[i]=='O'):
            r[i]=1
            y[i]=1
        elif(p[i]=='P'):
            r[i]=1
            b[i]=1
        elif(p[i]=='G'):
            b[i]=1
            y[i]=1
        elif(p[i]=='A'):
            r[i]=1
            y[i]=1
            b[i]=1
    sum = 0
    sr = "".join(str(i) for i in r)
    sr = list(sr.split("0"))
    for i in sr:
        if len(i)>0:
            sum+=1
    
    sb = "".join(str(i) for i in b)
    sb = list(sb.split("0"))
    for i in sb:
        if len(i)>0:
            sum+=1
    
    sy = "".join(str(i) for i in y)
    sy = list(sy.split("0"))
    for i in sy:
        if len(i)>0:
            sum+=1
    
    print(f"Case #{x+1}: {sum}")
        
