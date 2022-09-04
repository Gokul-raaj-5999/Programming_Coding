erica=input()
bob=input()
et=0
bt=0
for i in range(0,len(erica),1):
    if(erica[i]=="E"):
        et+=1
    elif(erica[i]=="M"):
        et+=3
    elif(erica[i]=="H"):
        et+=5
    if(bob[i]=="E"):
        bt+=1
    elif(bob[i]=="M"):
        bt+=3
    elif(bob[i]=="H"):
        bt+=5
if(et==bt):
    print("Tie")
elif(et>bt):
    print("Erica wins")
else:
    print("Bob wins")