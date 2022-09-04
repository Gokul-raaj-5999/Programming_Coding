def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string)-k+1,k):
        a=''
        b=string[i:i+k]
        #print(b)
        for j in b:
            if j not in a:
                a+=j
        print(a)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#############################################################################
"""
INPUT:
    AABCAAADA
    3
OUTPUT:
    AB
    CA
    AD
"""
