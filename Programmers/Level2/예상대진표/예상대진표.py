def solution(n, a, b):

    return ((a - 1) ^ (b - 1)).bit_length()


n, a, b = 8, 4, 7
print(solution(n, a, b))
