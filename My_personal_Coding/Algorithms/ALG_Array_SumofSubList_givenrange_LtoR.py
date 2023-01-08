# for this u have a array of n len 
# eg arr = [ 1 2 3 4 5 6 7 8 9 10 11 12 13 14]
# in this case u r given with the lower and upper length u have to find the sum of 
# elements that of that len so i this case u use this kind of algrothums 
# arr = [ 1 2 3 4 5 6 7 8 9 10 11 12 13 14] to find its sum and add it to a new list b[-1]
# so it will become 
# b = [1 3 6 10 15 21 28 36 45 55 66 72 85 99]
# and now what we do we subract b[r] - b[l-1] 
# if l == 0 then we make this b[r] thats all.


n = int(input())
v = list(map(int, input().split()))
m = int(input())
a = [v[0]]
for i in range(1, n):
    a.append(a[-1]+ v[i])

for _ in range(0, m):
    l, r = list(map(int, input().split()))
    if l == 0:
        print(a[r])
    else:
        print( a[r] - a[l-1])
