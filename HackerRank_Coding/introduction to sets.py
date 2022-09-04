def average(array):
    # your code goes here
    suma = sum(set(array))
    lena = len(set(array))
    return(suma/lena)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#########################################################################
"""
INPUT:
    10
    161 182 161 154 176 170 167 171 170 174

OUTPUT:
    169.375
"""
