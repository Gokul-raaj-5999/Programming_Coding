def minn(i, f):
    m = 100
    for j in f:
        y = min( abs(ord(i)-ord(j)) , 26-abs(ord(i)-ord(j)) )
        if(m > y):
            m = y
    return(m)

for x in range (0,int(input())):
    s = str(input())
    f = str(input())
    sum = 0
    for i in s:
        if( i not in f):
            m = minn(i,f)
            sum+=m
    print(f"Case #{x+1}: {sum}")
