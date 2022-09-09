def check(l,s):
    if(l>=7 and lowercase(s) and numberlength(s) and uppercase(s) and specfunction(s)):
        return(True)
    else:
        return(False)
#pls add a function for checking isnumeric()
def lowercase(s):
    for i in s:
        if(i.islower()):
            return(True)
def specfunction(s):
    splst = [ '#','@','*','&']
    for i in s:
        if(i in splst):
            return(True)
def uppercase(s):
    for i in s:
        if(i.isupper()):
            return(True)


for t in range (int(input())):
    l = int(input())
    s = str(input())
    if(check(l,s)):
        print(f'Case #{t+1}: {s}')
    else:
        if(lowercase(s)!= True):
            s+='a'
        if(uppercase(s)!= True):
            s+='A'
        if(specfunction(s)!= True):
            s+='@'
        if(numberlength(s)!= True):
            s+= '1'
        if(len(s)<7):
            x = 7 - len(s)
            s+= '1'*x
        print(f'Case #{t+1}: {s}')
        
        
        
 
