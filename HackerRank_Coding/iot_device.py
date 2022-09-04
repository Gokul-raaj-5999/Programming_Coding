devicenames=input().split()


exist=dict()
for i in range(0,len(devicenames),1):
    exist[devicenames[i]]=exist.get(devicenames[i],0)+1
    a=exist[devicenames[i]]
    if a>1:
        devicenames[i]+=str(a-1)
print(devicenames)
            