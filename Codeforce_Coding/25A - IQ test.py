n = int(input())
arr = list(map(int, input().split()))
eve = []
odd = []

for  i in arr:
    if i%2==0:
        eve.append(i)
    else:
        odd.append(i)
# print(eve,odd)

if(len(eve) < len(odd)):
    print(arr.index(eve[0])+1)
else:
    print(arr.index(odd[0])+1)
