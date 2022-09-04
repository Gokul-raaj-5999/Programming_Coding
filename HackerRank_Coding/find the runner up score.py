if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
final=list()
for i in arr:
    if i in final:continue
    final.append(i)
final.sort(reverse=True)
print(final[1])

##########################################################################
"""
INPUT:
    5
    2 3 6 6 5
    
OUTPUT:
    5
"""
