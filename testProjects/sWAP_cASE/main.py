#!/usr/bin/python3

def swap_case(s):
    li = list(s)
    x = 0
    while x < len(li):
        if li[x].islower():
            li[x] = li[x].upper()
        elif li[x].isupper():
            li[x] = li[x].lower()
        x+=1
    return "".join(li)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
