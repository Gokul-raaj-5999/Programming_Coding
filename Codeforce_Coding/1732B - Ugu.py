def solve():
    n = int(input())
    a = input()
    a = [int(x) for x in a]
    # print(a)

    f = 0
    count = 0

    for i in range(0, n-1):
        if a[i] == 1:
            f = 1
        if f == 1 and a[i] != a[i+1]:
            count += 1
    return count

            

for t in range(0, int(input())):
    print( solve() )