a = 'qwertyuiop'
b = 'asdfghjkl;'
c = 'zxcvbnm,./'

stt = input()
s = input()
op = ''
if stt == 'R':
    for i in s:
        if i in a:
            ind = a.index(i)
            # print(ind)
            op += a[ind-1]
        elif i in b:
            ind = b.index(i)
            # print(ind)
            op += b[ind-1]
        elif i in c:
            ind = c.index(i)
            # print(ind)
            op += c[ind-1]
    print(op)

else:
    for i in s:
        if i in a:
            ind = a.index(i)
            # print(ind)
            op += a[ind+1]
        elif i in b:
            ind = b.index(i)
            # print(ind)
            op += b[ind+1]
        elif i in c:
            ind = c.index(i)
            # print(ind)
            op += c[ind+1]
    print(op)

