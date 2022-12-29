# dp time comp - O(NxM)

def lcs(str1 , str2):
    mad, new = len(str1), len(str2)
    previous, current = [0]*(new+1), [0]*(new+1)
    for i in range(1, mad+1):
        for j in range(1, new+1):
            if str1[i-1] == str2[j-1]:
                current[j] = 1 + previous[j-1]
            else:
                if current[j-1] > previous[j]:
                    current[j] = current[j-1]
                else:
                    current[j] = previous[j]
            print(previous, current)
        current, previous = previous, current
    return previous[new]


for i in range(int(input())):
    n=int(input())
    s1=input()
    s2=input()
    print(lcs(s1,s2))


"""
ip1 = abcdef
ip2 = bhchdh

in this ab c def
         bhchdh
         | | |
         1 2 3

so we have 3 char of max length in comparing this two strings 



"""