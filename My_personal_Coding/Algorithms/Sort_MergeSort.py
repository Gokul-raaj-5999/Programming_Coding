def merger(a):
    if len(a) > 1:
        mid = (len(a)//2)
        l = a[:mid]
        r = a[mid:]

        merger(l) #for dividing 
        merger(r) #for dividing

        i = j = k = 0
        while i < len(l) and j < len(r):  #for conquering 
            if l[i] < r[j]:
                a[k] = l[i]
                i += 1
            else:
                a[k] = r[j]
                j +=1
            k += 1
        while i < len(l):  #end case for left of induvial element at frent 
            a[k] = l[i]
            i += 1
            k += 1
        while j < len(r):  #end case for left of induval element at last 
            a[k] = r[j]
            j += 1
            k += 1


a = [9,8,7,6,5,4,3,2,1]
print(a)
merger(a)
print(a)
