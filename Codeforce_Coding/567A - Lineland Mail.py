n = int(input())
a = list(map(int, input().split()))

for i in range(0, n):
    if i == 0:
        # print('---0')
        n = abs(a[i]-a[i+1])
    elif i == len(a)-1:
        # print('---1')
        n = abs(a[i-1]-a[i])
    else:
        # print('---2')
        n = min(abs(a[i]-a[i-1]), abs(a[i]-a[i+1]))
    
    if i ==0 :
        m = abs(a[i]-a[-1])
    elif i == len(a)-1:
        m = abs(a[i]- a[0])
    else:
        m = max( abs(a[i]-a[0]), abs(a[i]-a[-1]) )
    print(n, m)
    # print()

