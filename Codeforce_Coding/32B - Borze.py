s = input()
op = ''
i = 0
while(i< len(s)):
    if(s[i] == '.'):
        op+='0'
        i+=1
    elif(s[i] == '-'):
        i+=1
        if(s[i] == '.'):
            op+='1'
        else:
            op+='2'
        i+=1
print(op)
        

"""
B. Borze
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Ternary numeric notation is quite popular in Berland. To telegraph the ternary number the Borze alphabet is used. Digit 0 is transmitted as «.», 1 as «-.» and 2 as «--». You are to decode the Borze code, i.e. to find out the ternary number given its representation in Borze alphabet.

Input
The first line contains a number in Borze code. The length of the string is between 1 and 200 characters. It's guaranteed that the given string is a valid Borze code of some ternary number (this number can have leading zeroes).

Output
Output the decoded ternary number. It can have leading zeroes.

Examples
inputCopy
.-.--
outputCopy
012
inputCopy
--.
outputCopy
20
inputCopy
-..-.--
outputCopy
1012
"""
