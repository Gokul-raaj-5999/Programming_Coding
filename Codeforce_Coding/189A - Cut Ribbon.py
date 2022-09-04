// working but its working only in pypy3 but not in python soo to make it faster have added Fast_IO
import os, sys
from io import BytesIO, IOBase
 
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, 8192))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, 8192))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

n,a,b,c = list(map(int,input().split()))
count = 0
i = 0
while (i*a <=n ):
    j = 0
    while((i*a + j*b) <= n ):
        k = int(n- i*a - j*b)//c
        if(i*a + j*b + k*c == n):
            count = max(i+j+k, count)
        j+=1
    i+=1

print(int(count))


// my code its on DP, gave me TLE over 1000 loops in for loop but have correct logic
masterflag = 1
count = 0
lastflag = 1 

def functwo(n,a,b,c,count,masterflag,total,lastflag):
    flag = 1
    while(flag == 1 and n >= b):
        n-=b
        count+=1
        if(n%a==0):
            count+= n//a
            masterflag = 0
            flag = 0
            return(n,count,masterflag,lastflag)
        else:
            flag = 1
    else:
        n = total
        count = 0
        n = n - (c*lastflag)
        count += lastflag
        lastflag += 1
        if(n == 0):
            masterflag = 0
            return(n,count,masterflag,lastflag)
        else:
            return(n,count,masterflag,lastflag)
        
 
n,a,b,c = list(map(int, input().split()))
arr = [a,b,c]
arr.sort()
total = n
a,b,c = arr[0],arr[1],arr[2]
if(n%a==0):
    count+= n//a
else:
    while(masterflag == 1):
        n,count,masterflag,lastflag = functwo(n,a,b,c,count,masterflag,total,lastflag)
print(count)

"""
A. Cut Ribbon
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Polycarpus has a ribbon, its length is n. He wants to cut the ribbon in a way that fulfils the following two conditions:

After the cutting each ribbon piece should have length a, b or c.
After the cutting the number of ribbon pieces should be maximum.
Help Polycarpus and find the number of ribbon pieces after the required cutting.

Input
The first line contains four space-separated integers n, a, b and c (1 ≤ n, a, b, c ≤ 4000) — the length of the original ribbon and the acceptable lengths of the ribbon pieces after the cutting, correspondingly. The numbers a, b and c can coincide.

Output
Print a single number — the maximum possible number of ribbon pieces. It is guaranteed that at least one correct ribbon cutting exists.

Examples
inputCopy
5 5 3 2
outputCopy
2
inputCopy
7 5 5 2
outputCopy
2
Note
In the first example Polycarpus can cut the ribbon in such way: the first piece has length 2, the second piece has length 3.

In the second example Polycarpus can cut the ribbon in such way: the first piece has length 5, the second piece has length 2.
"""
