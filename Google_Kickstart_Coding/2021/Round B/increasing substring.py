for x in range(1, int(input())+1):
    n = int(input())
    s = str(input())
    lst = [1]
    count = 1
    for i in range(0,n-1):
        if(s[i]<s[i+1]):
            count+=1
        else:
            count = 1
        lst.append(count)
    st = " ".join(str(i) for i in lst)
    print(f"Case #{x}: {st}")
        
