#!/usr/bin/python3

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    i = 0
    s = 0
    for x in student_marks[query_name]:
        s = s+x
        i = i+1
    c = "{:.2f}".format(float(s/i))
    print(c)
