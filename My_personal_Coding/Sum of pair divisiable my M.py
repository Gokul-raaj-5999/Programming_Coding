
"""
formula = (a[i] + a[j])%b = 0 ->  required
so  (a[i]%b + a[j]%b )%b = 0
"""

a = list(map(int, input().split()))
b = int(input())
lst = [0]*b
print(lst)
for i in a:
    ind = i%b
    lst[ind] += 1
print(lst)

sum = 0
for i in range(1, len(lst)//2+1):
    sum += min(lst[i], lst[b-i])

sum += lst[0]//2
print(sum)


