def solution(x):
    answer = True
    numbers = map(int, list(str(x)))
    total = sum(numbers)
    if x % total:
        answer = False
    else:
        answer = True
    return answer

x = 10
print(solution(x))