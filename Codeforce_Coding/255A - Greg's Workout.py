n = int(input())
ar = list(map(int, input().split()))

dic = {'chest': 0, 'biceps': 0, 'back': 0}
f = 1
for i in ar:
    if f == 1:
        dic['chest'] += i
        f+=1
    elif f == 2:
        dic['biceps']+= i
        f += 1
    elif f == 3:
        dic['back'] += i
        f = 1

max = 0
# print(dic)
for i in dic:
    if dic[i] > max:
        op = i
        max = dic[i]
print(op)
    
    

"""
A. Greg's Workout
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Greg is a beginner bodybuilder. Today the gym coach gave him the training plan. All it had was n integers a1, a2, ..., an. These numbers mean that Greg needs to do exactly n exercises today. Besides, Greg should repeat the i-th in order exercise ai times.

Greg now only does three types of exercises: "chest" exercises, "biceps" exercises and "back" exercises. Besides, his training is cyclic, that is, the first exercise he does is a "chest" one, the second one is "biceps", the third one is "back", the fourth one is "chest", the fifth one is "biceps", and so on to the n-th exercise.

Now Greg wonders, which muscle will get the most exercise during his training. We know that the exercise Greg repeats the maximum number of times, trains the corresponding muscle the most. Help Greg, determine which muscle will get the most training.

Input
The first line contains integer n (1 ≤ n ≤ 20). The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 25) — the number of times Greg repeats the exercises.

Output
Print word "chest" (without the quotes), if the chest gets the most exercise, "biceps" (without the quotes), if the biceps gets the most exercise and print "back" (without the quotes) if the back gets the most exercise.

It is guaranteed that the input is such that the answer to the problem is unambiguous.

Examples
inputCopy
2
2 8
outputCopy
biceps
inputCopy
3
5 1 10
outputCopy
back
inputCopy
7
3 3 2 7 9 6 8
outputCopy
chest
Note
In the first sample Greg does 2 chest, 8 biceps and zero back exercises, so the biceps gets the most exercises.

In the second sample Greg does 5 chest, 1 biceps and 10 back exercises, so the back gets the most exercises.

In the third sample Greg does 18 chest, 12 biceps and 8 back exercises, so the chest gets the most exercise.
"""
