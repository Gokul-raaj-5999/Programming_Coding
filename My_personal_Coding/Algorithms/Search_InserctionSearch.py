def searchInsert(a, x):
    s = 0
    e = len(a)-1
    if x < a[0]:
        return 0
    elif x > a[-1]:
        return e+1
    while s<=e:
        mid = (s+e)//2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            s = mid+1
        else:
            e = mid -1
    if a[mid] < x:
        return mid+1
    else:
        return mid

a = list(map(int, input().split()))
x = int(input())
print('index is: ',searchInsert(a,x))