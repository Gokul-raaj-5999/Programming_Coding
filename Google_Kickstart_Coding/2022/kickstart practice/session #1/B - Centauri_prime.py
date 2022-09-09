volu = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

def solve():
    s = input()
    op = ''
    if s[-1] in volu:
        return (s+' is ruled by Alice.')
    elif s[-1] not in ['y', 'Y']:
        return (s+' is ruled by Bob.')
    else:
        return (s+' is ruled by nobody.')
    
    return (sum(ar)%k)
    
for t in range(0, int(input())):
    ans = solve()
    # s = ' '.join(str(x) for x in ans)
    print(f'Case #{t+1}: {ans}')
    

"""

Centauri Prime (5pts, 7pts)

Practice Submissions
Attempt 2
S
check
check
Sep 3 2022, 22:48
remove_red_eye
Attempt 1
Sample Failed: WA
Sep 3 2022, 22:48
remove_red_eye
Last updated: Sep 3 2022, 22:38

PROBLEM
ANALYSIS
Problem
Download the Starter Code!
Alice and Bob are playing the game called Centauri Prime. Centauri Prime represents a planet which is split into several independent kingdoms. Before they start playing the game, they have to choose rulers for each kingdom. Alice and Bob mutually decided to distribute kingdoms based on the letter the kingdom's name ended with. Alice loves vowels and decided to rule kingdoms whose names ended in a vowel. Bob loves consonants and decided to rule kingdoms whose names ended in a consonant. Both of them do not like the letter 'y'(case insensitive) and thus, all kingdoms whose names ended in the letter 'y' are left without a ruler. Can you write a program that will determine the rulers of several kingdoms, given the kingdoms' names?

Input
The first line of the input gives the number of test cases, T. T lines follow, each one containing the name of one kingdom. Kingdom names will consist of only lower case English letters, starting with a capital letter. There will be no other characters on any line, and no empty lines.
List of vowels for this problem is ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'].

Output
For each test case, output one line containing Case #x: K is ruled by Y., where x is the case number (starting from 1), K is the kingdom name, and Y is either Alice, Bob or nobody.

Be careful with capitalization and the terminating period. Your output must be in exactly this format. See the examples below.

Limits
Time limit: 30 seconds.
Memory limit: 1 GB.
1≤T≤300.
Test Set 1
Each kingdom name will have between 3 and 20 letters.

Test Set 2
Each kingdom name will have at most 100 letters.

Sample
Sample Input
save_alt
content_copy
3
Mollaristan
Auritania
Zizily
Sample Output
save_alt
content_copy
Case #1: Mollaristan is ruled by Bob.
Case #2: Auritania is ruled by Alice.
Case #3: Zizily is ruled by nobody.
In Sample Case #1, the name of the kingdom ends with 'n' which is a consonant and thus, it is ruled by Bob.

In Sample Case #2, the name of the kingdom ends with an 'a' which is a vowel and thus, it is ruled by Alice.

In Sample Case #3, the name of the kingdom ends with 'y' which is not liked by both of them and thus, it is ruled by nobody.
"""
