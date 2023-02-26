pi = '314159265358979323846264338327'


def solve():
    n = input()
    count = 0
    for i in range (0, len(n)):
        if n[i] == pi[i]:
            count += 1
        else:
            return count
    
    return count 

for t in range(0, int(input())):
    print(solve())