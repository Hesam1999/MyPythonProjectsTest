import textwrap

def wrap(string, max_width):
    li = []
    s = 0
    for x in string:
        if s == max_width:
            li.append("\n")
            li.append(x)
            s = 0
        elif s < max_width and s >= 0:
            li.append(x)
            s+=1
    return "".join(li)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)