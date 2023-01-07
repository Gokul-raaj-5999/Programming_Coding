n = int(input())
dic = {}
s = input()

for i in range(0, n-1):
    ss = s[i:i+2]
    if ss in dic:
        dic[ss] += 1
    else:
        dic[ss] = 1
# print(dic)
a = sorted(dic, key= dic.get)
print(a[-1])


"""
a = sorted(dic, key= dic.get) -> sort using value 
a = sorted(dic) -> sort using key, by default 
"""