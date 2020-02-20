# Problem [4875] : Forth

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    data = list(input().split())
    size = len(data)
    stack = list()
    flag = 0
    for i in range(size-1):  
        if data[i].isdigit():
            stack.append(data[i])
        else:
            try:  
                n2 = int(stack.pop())
                n1 = int(stack.pop())

                if data[i] == "+": result = n1 + n2
                elif data[i] == "-": result = n1 - n2
                elif data[i] == "/": result = n1 // n2
                elif data[i] == "*": result = n1 * n2

                stack.append(str(result))

            except: 
                flag = 1
    if flag == 0 and len(stack) == 1:
        print('#{} {}'.format(tc,stack[0]))

    elif flag == 1 or len(stack)>1:
        print('#{} {}'.format(tc,'error'))