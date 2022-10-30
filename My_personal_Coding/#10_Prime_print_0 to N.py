#print 0 to n, all prime number which are all in between 0 - n.

def isPrime(n):
    if(n==1 or n==0):
        return False
    for i in range(2,int(n**(1/2))+1):
        if(n%i==0):
            return False
        
    return True

N = 100
for i in range(1,N+1):
    if(isPrime(i)):
        print(i,end=" ")
