for _ in range(0, int(input())):
    p, m = map(int, input().split())
    print(min( min(p,m), (p+m)//4) )
    
        


"""
B. Team Composition: Programmers and Mathematicians
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
The All-Berland Team Programming Contest will take place very soon. This year, teams of four are allowed to participate.

There are a programmers and b mathematicians at Berland State University. How many maximum teams can be made if:

each team must consist of exactly 4 students,
teams of 4 mathematicians or 4 programmers are unlikely to perform well, so the decision was made not to compose such teams.
Thus, each team must have at least one programmer and at least one mathematician.

Print the required maximum number of teams. Each person can be a member of no more than one team.

Input
The first line contains an integer t (1≤t≤104) —the number of test cases.

This is followed by descriptions of t sets, one per line. Each set is given by two integers a and b (0≤a,b≤109).

Output
Print t lines. Each line must contain the answer to the corresponding set of input data — the required maximum number of teams.

Example
inputCopy
6
5 5
10 1
2 3
0 0
17 2
1000000000 1000000000
outputCopy
2
1
1
0
2
500000000
Note
In the first test case of the example, two teams can be composed. One way to compose two teams is to compose two teams of 2 programmers and 2 mathematicians.

In the second test case of the example, only one team can be composed: 3 programmers and 1 mathematician in the team.
"""
