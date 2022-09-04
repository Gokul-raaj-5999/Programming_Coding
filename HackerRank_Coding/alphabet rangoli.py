def print_rangoli(size):
    # your code goes here
    alp=list()
    alph = 'a'
    for i in range(0, 26):
        alp.append(alph)
        alph=chr(ord(alph) + 1)
##############top cone################################
    j=0
    for i in range(size-1,-1,-1):
        tem=''
        j+=1
        for k in range(i,size,1):
            x=str(alp[k])
            tem=tem+str('-')
            tem=tem+str(x)
        if(j==1):
            print(tem[1:].center(size*size-8,'-'))
            continue
        t=(tem[::-1])
        tem=t[0:-3]+tem[0:]
        print(tem.center(size*size-8,'-'))
################bottom cone###########################
    for i in range(1,size,1):
        tem=''
        j-=1
        for k in range(i,size,1):
            x=str(alp[k])
            tem=tem+str('-')
            tem=tem+str(x)
        if(j==1):
            print(tem[1:].center(size*size-8,'-'))
            continue
        t=(tem[::-1])
        tem=t[0:-3]+tem[0:]
        print(tem.center(size*size-8,'-'))
   #alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#################################################################################################3
"""
INPUT:
    5

OUTPUT:

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
