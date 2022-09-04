s = str(input())
low = []
for i in range(0,len(s)):
    if(s[i].islower()):
        low.append(i)
# print(low)
if(len(low) == 1):
    if(low[0]==0):
        x = s.lower()
        print(x.capitalize())
    else:
        print(s)
elif(len(low)==0):
    print(s.lower())
else:
    print(s)
    
