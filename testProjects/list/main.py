#!/usr/bin/python3

if __name__ == '__main__':
    N = int(input())
    l = []
    for x in range(N):
        il = input().split()
        if il[0] == "insert":
            l.insert(int(il[1]), int(il[2]))
        elif il[0] == "print":
            print(l)
        elif il[0] == "remove":
            l.remove(int(il[1]))
        elif il[0] == "append":
            l.append(int(il[1]))
        elif il[0] == "sort":
            l.sort()
        elif il[0] == "pop":
            l.pop()
        elif il[0] == "reverse":
            l.reverse()
