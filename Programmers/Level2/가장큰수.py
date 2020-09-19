def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: (x[0], x[1%len(x)], x[2%len(x)], x[3%len(x)]), reverse=True)
    return str(int(''.join(numbers)))

numbers = [3, 30, 34, 5, 9]

print(solution(numbers))