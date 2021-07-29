def solution(numbers):
    answer = []

    for num in numbers:
        binary = list('0' + bin(num)[2:])
        idx = ''.join(binary).rfind('0')
        binary[idx] = '1'

        if num % 2 == 1:
            binary[idx + 1] = '0'

        answer.append(int(''.join(binary), 2))

    return answer


numbers = [2, 7]
print(solution(numbers))
