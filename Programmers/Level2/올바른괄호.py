from collections import deque

def solution(s):
    answer = True
    stack = deque()
    s = deque(s)
    
    while s:
        temp = s.popleft()
        if temp == '(':
            stack.append(temp)
        else:
            if stack:
                temp = stack.pop()
                if temp != '(':
                    answer = False
                    break
            else:
                answer = False
                break
    
    if stack:
        answer = False
    return answer

s = "(())()"

print(solution(s))