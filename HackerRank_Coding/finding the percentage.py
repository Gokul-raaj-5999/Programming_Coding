if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
avg=0
count=0
for i in student_marks[query_name]:
    avg+=i
    count+=1
avg=(avg/count)
print("%.2f" %avg)

############################################################################
"""
SAMPLE1:
    INPUT:
        3
        Krishna 67 68 69
        Arjun 70 98 63
        Malika 52 56 60
        Malika
    OUTPUT:
        56.00

SAMPLE2:
    INPUT:
        2
        Harsh 25 26.5 28
        Anurag 26 28 30
        Harsh
    OUTPUT:
        26.50
"""
