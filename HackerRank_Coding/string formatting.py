def print_formatted(number):
    # your code goes here
    decimal=list()
    octal=list()
    hexa=list()
    binary=list()
    for i in range(1,number+1,1):
        decimal.append(str(int(i)))
        octal.append(str((oct(i).split('o'))[1]))
        hexa.append(str((hex(i).split('x'))[1]))
        binary.append(str((bin(i).split('b'))[1]))

    blen=len(binary[-1])
    dlen=len(decimal[-1])
    dlen=blen-dlen
    space=' '
    for i in range(number):
        print(decimal[i].rjust(blen,space),octal[i].rjust(blen,space),(hexa[i].upper()).rjust(blen,space),binary[i].rjust(blen,space))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

###############################################################################
"""
SAMPLE1:
    INPUT:
        2
    OUTPUT:
         1  1  1  1
         2  2  2 10
SAMPLE2:
    INPUT:
        17
    OUTPUT:
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
"""
