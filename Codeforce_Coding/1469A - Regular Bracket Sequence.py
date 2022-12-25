def solve():
    s = input()
    if len(s)%2 == 0 and s[0]!= ')' and s[-1] != '(':
        return 'Yes'
    return 'No'
    

for t in range(0, int(input())):
    print(solve())