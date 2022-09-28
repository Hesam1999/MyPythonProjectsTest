#!/usr/bin/python3

if __name__ == '__main__':

    list1 = []
    lowestNum = 200
    resualtscore = -100

    for _ in range(int(input())):
        name = input()
        score = float(input())

        list1.append([name, score])
        
        if score < lowestNum:
            lowestNum = score

    list1.sort(key=lambda x: x[1])
    list2 = []
    for x in list1:
        if x[1] > lowestNum:
            resualtscore = x[1]
            break
    for x in list1:
        if x[1] == resualtscore:
            list2.append(x)
    list2.sort()
    for x in list2:
        print(x[0])

    