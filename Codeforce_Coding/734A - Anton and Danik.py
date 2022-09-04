n = int(input())
s = str(input())
a,d = 0,0
for i in s:
    if(i=='A'):
        a+=1
    else:
        d+=1
if(a==d):
    print('Friendship')
elif(a>d):
    print('Anton')
else:
    print('Danik')
