alp = []
for i in range(ord('a'), ord('z')+1):
    for j in range(ord('a'), ord('z')+1):
        if chr(i) != chr(j):
            alp.append(str(chr(i)+chr(j)))

# print(alp)
for _ in range(0, int(input())):
    s = input()
    print(alp.index(s)+1)
    

"""
B. Dictionary
time limit per test2 seconds
memory limit per test512 megabytes
inputstandard input
outputstandard output
The Berland language consists of words having exactly two letters. Moreover, the first letter of a word is different from the second letter. Any combination of two different Berland letters (which, by the way, are the same as the lowercase letters of Latin alphabet) is a correct word in Berland language.

The Berland dictionary contains all words of this language. The words are listed in a way they are usually ordered in dictionaries. Formally, word a comes earlier than word b in the dictionary if one of the following conditions hold:

the first letter of a is less than the first letter of b;
the first letters of a and b are the same, and the second letter of a is less than the second letter of b.
So, the dictionary looks like that:

Word 1: ab
Word 2: ac
...
Word 25: az
Word 26: ba
Word 27: bc
...
Word 649: zx
Word 650: zy
You are given a word s from the Berland language. Your task is to find its index in the dictionary.

Input
The first line contains one integer t (1≤t≤650) — the number of test cases.

Each test case consists of one line containing s — a string consisting of exactly two different lowercase Latin letters (i. e. a correct word of the Berland language).

Output
For each test case, print one integer — the index of the word s in the dictionary.

Example
inputCopy
7
ab
ac
az
ba
bc
zx
zy
outputCopy
1
2
25
26
27
649
650
"""
