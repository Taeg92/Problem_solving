# Problem [9012] : 괄호

# from collections import deque
# import sys
# input = lambda : sys.stdin.readline()

T = int(input())
for tc in range(T):
    result = 'YES'
    data = list(input())
    i = 0
    flag = 0
    while len(data) != 0:
        if data[i] == '(':
            if data[i+1] == ')':
                data.pop(i)
                data.pop(i)
                flag = 1
        i += 1
        if flag == 1 and i >= len(data) - 1:
            i = 0
            flag = 0
        if flag == 0 and i == len(data) - 1:
            result = 'NO'
            break
    print(result)