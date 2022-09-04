# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
s=set()
for i in range(N):
    s.add(input())
print(len(s))

###############################################################################
"""
INPUT:
      7
      UK
      China
      USA
      France
      New Zealand
      UK
      France
OUTPUT:
      5
"""
