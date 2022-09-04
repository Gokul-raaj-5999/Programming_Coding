import math,sys
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
 
def callone(num):
    def prime(n):
        prime_flag = 0
        if(n > 2):
            for i in range(2, int(math.sqrt(n)) + 1):
                if (n % i == 0):
                    prime_flag = 1
                    break
            if (prime_flag == 0):
                return 1
            else:
                return 0
        else:
            return 0
        
    if(num > 4):
        x = math.sqrt(num)
        s = str(x)
        if(s[-2:] == '.0'):
            if(prime(x)):
                    return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0
        
def array(num):
    ele = 3
    primearr = set()
    while(ele < num+1):
        for i in range(2, int(math.sqrt(ele)) + 1):
            if (ele % i == 0):
                break
        else:
            primearr.add(ele)
        ele+=1
    return(primearr)
 
def call(num):
    if(num > 4):
        x = math.sqrt(num)
        s = str(x)
        if(s[-2:] == '.0'):
            return 1
        else:
            return 0
    else:
        return 0
 
     
n = int(input())
arr = list(map(int, input().split()))
 
if len(arr) > 1:
    m = int(math.sqrt(max(arr)))
    primearr = array(m)
    for i in arr:
        if(i==4):
            print('YES')
        elif(i%2==0):
            print('NO')
        elif(call(i) and (int(math.sqrt(i)) in primearr)):
            print("YES")
        else:
            print("NO")
else:
    if(callone(arr[0])):
        print("YES")
    else:
        print("NO")
        
"""//TLE
import math

def callone(num):
    def prime(n):
        prime_flag = 0
        if(n > 2):
            for i in range(2, int(math.sqrt(n)) + 1):
                if (n % i == 0):
                    prime_flag = 1
                    break
            if (prime_flag == 0):
                return 1
            else:
                return 0
        else:
            return 0
        
    if(num > 4):
        x = math.sqrt(num)
        s = str(x)
        if(s[-2:] == '.0'):
            if(prime(x)):
                    return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0
        
def array(num):
    ele = 3
    primearr = []
    while(ele < num+1):
        for i in range(2, int(math.sqrt(ele)) + 1):
            if (ele % i == 0):
                break
        else:
            primearr.append(ele)
        ele+=1
    return(primearr)

def call(num):
    if(num > 4):
        x = math.sqrt(num)
        s = str(x)
        if(s[-2:] == '.0'):
            return 1
        else:
            return 0
    else:
        return 0
        
n = int(input())
arr = list(map(int, input().split()))

if len(arr) > 1:
    m = int(math.sqrt(max(arr)))
    primearr = array(m)
    # print(primearr)
    for i in arr:
        if(i==4):
            print('YES')
        elif(i%2==0):
            print('NO')
        elif(call(i) and (int(math.sqrt(i)) in primearr)):
            print("YES")
        else:
            print("NO")
else:
    if(callone(arr[0])):
        print("YES")
    else:
        print("NO")
 """
"""
//array type method same TLE

import math
 
def array(num):
    ele = 3
    primearr = []
    while(ele < num+1):
        for i in range(2, int(math.sqrt(ele)) + 1):
            if (ele % i == 0):
                break
        else:
            primearr.append(ele)
        ele+=1
    return(primearr)
    
def call(num):
    if(num > 4):
        x = math.sqrt(num)
        s = str(x)
        if(s[-2:] == '.0'):
            return 1
        else:
            return 0
    else:
        return 0
        
n = int(input())
arr = list(map(int, input().split()))
m = int(math.sqrt(max(arr)))
# print(m)
primearr = array(m)
# print(primearr)
 
for i in arr:
    if(i==4):
        print('YES')
    elif(i%2==0):
        print('NO')
    elif(call(i) and (int(math.sqrt(i)) in primearr)):
        print("YES")
    else:
        print("NO")
"""
 """
 B. T-primes
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
We know that prime numbers are positive integers that have exactly two distinct positive divisors. Similarly, we'll call a positive integer t Т-prime, if t has exactly three distinct positive divisors.

You are given an array of n positive integers. For each of them determine whether it is Т-prime or not.

Input
The first line contains a single positive integer, n (1 ≤ n ≤ 105), showing how many numbers are in the array. The next line contains n space-separated integers xi (1 ≤ xi ≤ 1012).

Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is advised to use the cin, cout streams or the %I64d specifier.

Output
Print n lines: the i-th line should contain "YES" (without the quotes), if number xi is Т-prime, and "NO" (without the quotes), if it isn't.

Examples
inputCopy
3
4 5 6
outputCopy
YES
NO
NO
Note
The given test has three numbers. The first number 4 has exactly three divisors — 1, 2 and 4, thus the answer for this number is "YES". The second number 5 has two divisors (1 and 5), and the third number 6 has four divisors (1, 2, 3, 6), hence the answer for them is "NO".

"""
