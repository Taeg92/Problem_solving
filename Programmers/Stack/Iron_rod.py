# Problem : 쇠막대기

from collections import deque

def solution(arrangement):
    stack = deque()
    arr = arrangement.replace('()','L')
    rod = deque(arr)
    answer = 0
    while len(rod) != 0:
        temp = rod.popleft()
        if temp == '(' :
            stack.append(temp)
            answer += 1      
        elif temp == 'L':
            answer += len(stack)
        else:
           stack.pop()
    return answer


arrangement = '()(((()())(())()))(())'
print(solution(arrangement))

arrangement = '(())'
print(solution(arrangement))