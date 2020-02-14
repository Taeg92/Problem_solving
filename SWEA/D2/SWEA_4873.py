# Problem [4873] : 반복문자 지우기


T = int(input())

for tc in range(1,T+1):
    data = list(input())
    i = 0
    flag = 0
    while 1:
        if data[i] == data[i+1]:
            data.pop(i)
            data.pop(i)
            flag = 1
        i += 1
        if flag == 1 and i >= len(data) - 1:
            i = 0
            flag = 0
        if flag == 0 and i >= len(data) - 1:
            break
    print('#{} {}'.format(tc,len(data))) 


# T = int(input())

# for tc in range(1,T+1):
#     stack = []
#     D = input()
#     for c in D:
#         if not stack:
#             if stack[-1] == c:
#                 stack.pop()
#             else:
#                 stack.append(c)
#         else:
#             stack.append(c)
#     print('{}'.format(tc,len(stack)))