# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
dash='-'
welcome='WELCOME'
pattern='.|.'
patcount=1
for i in range(int((n-1)/2)):
    final=(dash*int((m-(patcount*3))/2))+pattern*patcount+(dash*int((m-(patcount*3))/2))
    print(final)
    patcount+=2
final=(dash*int((m-7)/2))+welcome+(dash*int((m-7)/2))
print(final)
for i in range(int((n-1)/2)):
    patcount-=2
    final=(dash*int((m-(patcount*3))/2))+pattern*patcount+(dash*int((m-(patcount*3))/2))
    print(final)

##############################################################################################
"""
INPUT:
        7 21

OUTPUT:
        ---------.|.---------
        ------.|..|..|.------
        ---.|..|..|..|..|.---
        -------WELCOME-------
        ---.|..|..|..|..|.---
        ------.|..|..|.------
        ---------.|.---------
"""
