#boubble sort with time complexity O(n*(n-1)) and O(n*)

a = list(map(int, input().split()))
aa = a.copy()
n = len(a)
change = len(a)
steps = 0
while change > 0:   # set a value called changes soo if in that perticular iteration we dont have any changes we end that loop entairy
    change = 0      # workes good when u have more no.of duplicate elementes, if all are distinc will work  like O(n*(n-1))
    for i in range(0, n-1):
        if a[i] > a[i+1]:
            change += 1
            a[i], a[i+1] = a[i+1], a[i]
    print(steps, '---',a)
    steps += 1

print(a)
steps = 0
while n-1:          # a normail bouble sort
    change = 0
    for i in range(0, len(aa)-1):
        if aa[i] > aa[i+1]:
            change += 1
            aa[i], aa[i+1] = aa[i+1], aa[i]
    print(steps, '---',aa)
    steps += 1
    n-=1

print(a)
    
