def difference(one, two):
    sum = 0
    for i in range(0, len(one)):
        sum += abs( ord(one[i]) - ord(two[i]) )
    return sum

for _ in range(0, int(input())):
    n, m = map(int, input().split())
    ar = []
    dic = {}
    for i in range(0, n):
        s = input()
        ar.append(s)
        
    # print(ar)
    flag = 0
    for i in range(0, len(ar)):
        if ar[i] in ar[i+1:]:
            flag = 1
            break
        
    if flag == 0:
        for s in ar:
            tem = []
            for ss in ar:
                if s != ss:
                    # print(s,ss)
                    tem.append(difference(s, ss))
            dic[s] = tem
            
        # print(dic)
        mimun = 10000000000000000
        for i in dic:
            l = list(dic[i])
            if len(l) > 0:
                m = min(l)
            else:
                m = 0
            if m < mimun:
                mimun = m
                
        print(mimun)    
        # print()
    else:
        print(0)
        
        
        

"""
C. Most Similar Words
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given n words of equal length m, consisting of lowercase Latin alphabet letters. The i-th word is denoted si.

In one move you can choose any position in any single word and change the letter at that position to the previous or next letter in alphabetical order. For example:

you can change 'e' to 'd' or to 'f';
'a' can only be changed to 'b';
'z' can only be changed to 'y'.
The difference between two words is the minimum number of moves required to make them equal. For example, the difference between "best" and "cost" is 1+10+0+0=11.

Find the minimum difference of si and sj such that (i<j). In other words, find the minimum difference over all possible pairs of the n words.

Input
The first line of the input contains a single integer t (1≤t≤100) — the number of test cases. The description of test cases follows.

The first line of each test case contains 2 integers n and m (2≤n≤50, 1≤m≤8) — the number of strings and their length respectively.

Then follows n lines, the i-th of which containing a single string si of length m, consisting of lowercase Latin letters.

Output
For each test case, print a single integer — the minimum difference over all possible pairs of the given strings.

Example
inputCopy
6
2 4
best
cost
6 3
abb
zba
bef
cdu
ooo
zzz
2 7
aaabbbc
bbaezfe
3 2
ab
ab
ab
2 8
aaaaaaaa
zzzzzzzz
3 1
a
u
y
outputCopy
11
8
35
0
200
4
Note
For the second test case, one can show that the best pair is ("abb","bef"), which has difference equal to 8, which can be obtained in the following way: change the first character of the first string to 'b' in one move, change the second character of the second string to 'b' in 3 moves and change the third character of the second string to 'b' in 4 moves, thus making in total 1+3+4=8 moves.

For the third test case, there is only one possible pair and it can be shown that the minimum amount of moves necessary to make the strings equal is 35.

For the fourth test case, there is a pair of strings which is already equal, so the answer is 0.

"""
