def solve():
    n = int(input())
    s = input()

    x,y = 0,0

    for i in s:
        if i == 'U':
            y += 1
        elif i == 'D':
            y -=1
        elif i == 'L':
            x -=1
        else:
            x += 1
        
        if x==1 and y ==1:
            return 'Yes'
    
    if x==1 and y ==1:
        return 'Yes'
    else:
        return 'No'

for t in range(0, int(input())):
    print(solve())