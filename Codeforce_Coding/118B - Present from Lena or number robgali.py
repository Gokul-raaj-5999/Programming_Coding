n = int(input())
lst = []
s = []
for i in range(0, n+1):
    s.append(i)
ss = " ".join( str(x) for x in s)
ss = ss + ss[-2::-1]
# print(ss)
mlen = len(ss)
print(' '*(mlen//2) + '0')
lst.append(ss)
for i in range(0, n):
    mid = len(ss)//2
    ss = ss[:mid-2] + ss[mid+2: ]
    # print(ss)
    lst.append(ss)

for i in range(n-1, 0, -1):
    print(' '*(mlen//2 - (len(lst[i])//2)), end= '' )
    print(lst[i])
for i in range(0, n):
    print(' '*(mlen//2 - (len(lst[i])//2)), end= '' )
    print(lst[i])
print(' '*(mlen//2) + '0')


"""
          0
        0 1 0
      0 1 2 1 0
    0 1 2 3 2 1 0
  0 1 2 3 4 3 2 1 0
0 1 2 3 4 5 4 3 2 1 0
  0 1 2 3 4 3 2 1 0
    0 1 2 3 2 1 0
      0 1 2 1 0
        0 1 0
          0
          
"""