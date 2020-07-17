def solution(n):
    answer = 0
    numbers = map(int, list(str(n)))
    answer = sum(numbers)
    return answer

n = 987
print(solution(n))