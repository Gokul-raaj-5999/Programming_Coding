from hashlib import new
from os import remove, rename
import string
from collections import OrderedDict

def solve():
    alp = list(string.ascii_lowercase)
    adic = {}
    for i in range(0, len(alp)):
        adic[alp[i]] = i+1

    s = list(input())
    l = len(s)
    opind = []
    opval = []
    opeind = []
    opeval = []
    dic = {}
    start = [adic[s[0]], s[0], 1]
    end = [adic[s[-1]], s[-1], l]
    for i in range(1, len(s)-1):
        dic[adic[s[i]]] = [s[i], i+1]

    v1, v2 = adic[s[0]], adic[s[-1]]
    opind.append(1)
    opval.append(start[0])
    opeind.append(l)
    opeval.append(end[0])

    m = max(v1, v2)
    print(dic)
    newdic = {}
    for i in dic:
        if i < m:
            newdic[i] = dic[i]

    mt = 2+ len(newdic)
    # print(newdic)
    newdic = OrderedDict(sorted(newdic.items()))

    for i in newdic:
        opind.append(newdic[i][1])
        opval.append(i)
    opind.extend(opeind)
    opval.extend(opeval)
    val = 0
    for i in range(0, len(opval)-1):
        val = val + abs(opval[i] - opval[i+1])

    print(val, mt)
    print(' '.join(str(x) for x in opind))


    # return


for t in range(0, int(input())):
    ans = solve()
    # print()



"""

6
logic
codeforces
bca
aaaaaaaaaaa
adbaadabad
to


In output m is the maximum number of visited tiles 
(i.e. number of jumps is m-1). In the first test case of 
the example there 3 jumps, i.e. m=4 visited tiles. Look into 
the picture for details.

"""