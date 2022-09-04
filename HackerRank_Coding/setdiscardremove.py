n = int(input())
s = set(map(int, input().split()))
no_of_commands=int(input())
for i in range(no_of_commands):
    command=input()
    if command=='pop':
        s.pop()
        continue
    command=command.split()
    if(command[0]=='remove'):
        s.remove(int(command[1]))
        continue
    if(command[0]=='discard'):
        s.discard(int(command[1]))
sum1=0
for i in s:
    sum1+=int(i)
print(sum1)

############################################################################
"""
INPUT:
          9
          1 2 3 4 5 6 7 8 9
          10
          pop
          remove 9
          discard 9
          discard 8
          remove 7
          pop
          discard 6
          remove 5
          pop
          discard 5
OUTPUT:
          4
"""
