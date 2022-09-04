for _ in range(int(input())):
    ln = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    # print(arr)
    alow = arr[:len(arr)//2]
    ahig = arr[len(arr)//2:]
    # print(alow,ahig)
    i = 0
    anhig = []
    while(i < len(ahig)):
        if(ahig[i] in alow):
            alow.append(ahig[i])
        else:
            anhig.append(ahig[i])
        # print(" ",i)
        i+=1
    # print(alow,anhig)
    if(len(alow) == len(anhig)):
        print("YES")
        op = []
        for i in range(0,len(anhig)):
            op.append(alow[i])
            op.append(anhig[i])
        for i in op:
            print(i,end= ' ')
        print("")
    else:
        print("NO")
        
// this is failling in 2nd test case and like showing """wrong answer Jury found the answer but participant didn't (test case 1435)"""
