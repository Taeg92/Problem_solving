def format_bin(n, val1, val2):
    binary = bin(val1 | val2)[2:]
    return '0' * (n-len(binary)) + binary


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        binary = format_bin(n, arr1[i], arr2[i])
        binary = binary.replace('1', '#')
        binary = binary.replace('0', ' ')
        answer.append(binary)

    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(n, arr1, arr2))
