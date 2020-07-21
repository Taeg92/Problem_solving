def solution(n):
    numbers = sorted(list(str(n)), reverse=True)
    answer = ''.join(numbers)
    return int(answer)

n = 118372
print(solution(n))