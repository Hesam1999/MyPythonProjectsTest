def count_substring(string, sub_string):
    n = 0
    s = 0
    for x in range(0, len(string)):
        if sub_string[0] == string[x]:
            for y in range(x, len(string)):
                if sub_string[s] == string[y]:
                    s+=1
                    if s == len(sub_string):
                        s = 0
                        n+=1
                        break
                elif s+1 >= len(sub_string):
                    s = 0
                    break
    return n

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)