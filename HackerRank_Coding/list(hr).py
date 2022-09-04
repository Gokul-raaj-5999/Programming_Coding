if __name__ == '__main__':
    N = int(input())
fo=list()
for i in range(0,N-1,1):
    cmd=input().split()
    if(cmd[0]=='insert'):fo.insert(int(cmd[1]),int(cmd[2]))
    if(cmd[0]=='print'):print(fo)
    if(cmd[0]=='remove'):fo.remove(int(cmd[1]))
    if(cmd[0]=='append'):fo.append(int(cmd[1]))
    if(cmd[0]=='sort'):fo.sort()
    if(cmd[0]=='pop'):fo.pop()
    if(cmd[0]=='reverse'):fo.reverse()
print(fo)

##############################################################################
"""
insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

INPUT:
    12
    insert 0 5
    insert 1 10
    insert 0 6
    print
    remove 6
    append 9
    append 1
    sort
    print
    pop
    reverse
    print

OUTPUT:
    [6, 5, 10]
    [1, 5, 9, 10]
    [9, 5, 1]
"""
