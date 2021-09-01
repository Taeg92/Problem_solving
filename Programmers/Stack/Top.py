# Problem : Top

from collections import deque

def solution(heights):
    answer = deque()
    flag = 0
    for i in range(len(heights)-1,0,-1):
        flag = 0
        for j in range(i-1,-1,-1):
            if heights[i] < heights[j]:
                answer.appendleft(j+1)
                flag = 1
                break
        if flag != 1:
            answer.appendleft(0)
    
    
    return list(answer)

heights = [6, 9, 5, 7, 4]
print(solution(heights))

heights = [3, 9, 9, 3, 5, 7, 2]
print(solution(heights))

heights = 	[1, 5, 3, 6, 7, 6, 5]
print(solution(heights))
