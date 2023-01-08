
def solve():
    n = input()
    arr = (n.split('1'))
    # print(arr)
    if n[0] != '1':
        return 'NO'

    for i in arr:
        if i == '4' or i == '44' or i == '':
            continue
        else:
            return 'NO'
    return 'YES'

print(solve())
