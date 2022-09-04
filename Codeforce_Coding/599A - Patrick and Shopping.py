a,b,c = list(map(int, input().split()))


if( a > b and a > c):
    dis = (b+c)*2
elif (b > a and b > c):
    dis = (a+c)*2
else:
    if(a+b < c):
        dis = (a+b)*2
    elif(a+b > c):
        dis  = (a+b+c)
    else:
        dis = (a+b+c)
print(dis)

"""
A. Patrick and Shopping
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Today Patrick waits for a visit from his friend Spongebob. To prepare for the visit, Patrick needs to buy some goodies in two stores located near his house. There is a d1 meter long road between his house and the first shop and a d2 meter long road between his house and the second shop. Also, there is a road of length d3 directly connecting these two shops to each other. Help Patrick calculate the minimum distance that he needs to walk in order to go to both shops and return to his house.


Patrick always starts at his house. He should visit both shops moving only along the three existing roads and return back to his house. He doesn't mind visiting the same shop or passing the same road multiple times. The only goal is to minimize the total distance traveled.

Input
The first line of the input contains three integers d1, d2, d3 (1 ≤ d1, d2, d3 ≤ 108) — the lengths of the paths.

d1 is the length of the path connecting Patrick's house and the first shop;
d2 is the length of the path connecting Patrick's house and the second shop;
d3 is the length of the path connecting both shops.
Output
Print the minimum distance that Patrick will have to walk in order to visit both shops and return to his house.

Examples
inputCopy
10 20 30
outputCopy
60
inputCopy
1 1 5
outputCopy
4
Note
The first sample is shown on the picture in the problem statement. One of the optimal routes is: house  first shop  second shop  house.

In the second sample one of the optimal routes is: house  first shop  house  second shop  house.

"""
