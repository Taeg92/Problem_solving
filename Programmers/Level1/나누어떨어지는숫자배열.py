def solution(arr, divisor):
    answer = []
    for num in arr:
        if not num % divisor:
            answer.append(num)
    if not answer:
        answer.append(-1)
    return sorted(answer)

arr = [2, 36, 1, 3]
divisor = 1

print(solution(arr, divisor))