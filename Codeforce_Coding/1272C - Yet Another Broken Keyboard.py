n, k = map(int, input().split())
s = input()
a = set(list(s))
ks = list(input().split())
remset = a - set(ks)

for i in remset:
    s = s.replace(i, ' ')

vec = list(s.split())
sum = 0
for i in vec:
    l = len(i)
    sum = sum + (l*(l+1)//2)

print(sum)


"""
C. Yet Another Broken Keyboard
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Recently, Norge found a string s=s1s2…sn consisting of n lowercase Latin letters. As an exercise to improve his typing speed, he decided to type all substrings of the string s. Yes, all n(n+1)2 of them!

A substring of s is a non-empty string x=s[a…b]=sasa+1…sb (1≤a≤b≤n). For example, "auto" and "ton" are substrings of "automaton".

Shortly after the start of the exercise, Norge realized that his keyboard was broken, namely, he could use only k Latin letters c1,c2,…,ck out of 26.

After that, Norge became interested in how many substrings of the string s he could still type using his broken keyboard. Help him to find this number.

Input
The first line contains two space-separated integers n and k (1≤n≤2⋅105, 1≤k≤26) — the length of the string s and the number of Latin letters still available on the keyboard.

The second line contains the string s consisting of exactly n lowercase Latin letters.

The third line contains k space-separated distinct lowercase Latin letters c1,c2,…,ck — the letters still available on the keyboard.

Output
Print a single number — the number of substrings of s that can be typed using only available letters c1,c2,…,ck.

Examples
inputCopy
7 2
abacaba
a b
outputCopy
12
inputCopy
10 3
sadfaasdda
f a d
outputCopy
21
inputCopy
7 1
aaaaaaa
b
outputCopy
0
Note
In the first example Norge can print substrings s[1…2], s[2…3], s[1…3], s[1…1], s[2…2], s[3…3], s[5…6], s[6…7], s[5…7], s[5…5], s[6…6], s[7…7].

"""