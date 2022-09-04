import math

def printDivisors(n) :
    i = 1
    arr = []
    while i <= math.sqrt(n):
        if (n % i == 0) :
            if (n / i == i) :
                arr.append(i)
            else :
                arr.append(i)
                arr.append(int(n/i))
        i = i + 1
    return(arr)
        
arr = printDivisors(int(input()))
print(len(arr)-1)

"""
A. Fafa and his Company
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Fafa owns a company that works on huge projects. There are n employees in Fafa's company. Whenever the company has a new project to start working on, Fafa has to divide the tasks of this project among all the employees.

Fafa finds doing this every time is very tiring for him. So, he decided to choose the best l employees in his company as team leaders. Whenever there is a new project, Fafa will divide the tasks among only the team leaders and each team leader will be responsible of some positive number of employees to give them the tasks. To make this process fair for the team leaders, each one of them should be responsible for the same number of employees. Moreover, every employee, who is not a team leader, has to be under the responsibility of exactly one team leader, and no team leader is responsible for another team leader.

Given the number of employees n, find in how many ways Fafa could choose the number of team leaders l in such a way that it is possible to divide employees between them evenly.

Input
The input consists of a single line containing a positive integer n (2 ≤ n ≤ 105) — the number of employees in Fafa's company.

Output
Print a single integer representing the answer to the problem.

Examples
inputCopy
2
outputCopy
1
inputCopy
10
outputCopy
3
Note
In the second sample Fafa has 3 ways:

choose only 1 employee as a team leader with 9 employees under his responsibility.
choose 2 employees as team leaders with 4 employees under the responsibility of each of them.
choose 5 employees as team leaders with 1 employee under the responsibility of each of them.
"""
