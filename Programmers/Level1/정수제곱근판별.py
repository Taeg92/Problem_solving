def solution(n):
    answer = 0
    if (n**0.5) % 1:
        answer = -1
    else:
        answer = int(((n**0.5)+1)**2)
    return answer

n = 121
print(solution(n))