def solution(a, b):
    answer = (abs(a-b)+1)*(a+b)//2
    return answer

a = 5
b = 3
print(solution(a, b))