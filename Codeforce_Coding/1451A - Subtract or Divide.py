for _ in range(0, int(input())):
    n = int(input())
    
    count = 0
    if n > 1:
        if n%2 == 0:
            while n>2:
                n = n//(n//2)
                count+=1
            
        else:
            count +=1
            n-=1
            while n>2:
                n = n//(n//2)
                count+=1
        
        print(count+1)
    else:
        print(0)
            

"""
A. Subtract or Divide
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Ridbit starts with an integer n.

In one move, he can perform one of the following operations:

divide n by one of its proper divisors, or
subtract 1 from n if n is greater than 1.
A proper divisor is a divisor of a number, excluding itself. For example, 1, 2, 4, 5, and 10 are proper divisors of 20, but 20 itself is not.

What is the minimum number of moves Ridbit is required to make to reduce n to 1?

Input
The first line contains a single integer t (1≤t≤1000) — the number of test cases.

The only line of each test case contains a single integer n (1≤n≤109).

Output
For each test case, output the minimum number of moves required to reduce n to 1.

Example
inputCopy
6
1
2
3
4
6
9
outputCopy
0
1
2
2
2
3
Note
For the test cases in the example, n may be reduced to 1 using the following operations in sequence

1
2→1
3→2→1
4→2→1
6→2→1
9→3→2→1
"""
