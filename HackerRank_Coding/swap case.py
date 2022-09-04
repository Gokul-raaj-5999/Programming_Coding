def swap_case(s):
    j=0
    newstr=''
    for i in s:
        if(i.isupper()==True):
            newstr+=i.lower()
            #print(i,"upper",newstr)
        elif(i.islower()==True):
            newstr+=i.upper()
            #print(i,"lower",newstr)
        else:
            newstr+=i
            #print(i,"speci",newstr)
    return(newstr)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

###############################################################################
"""
INPUT:
HackerRank.com presents "Pythonist 2".

OUTPUT:
hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""
