import sys


def solution(N, A):
    # write your code in Python 3.6
    result = [0] * N
    max_val = 0
    is_changed = False
    for num in A:
        if num <= N:
            result[num - 1] += 1
            if max_val < result[num - 1]:
                max_val = result[num - 1]
                is_changed = True
        elif is_changed:
            result = [max_val] * N
            is_changed = False
    return result


N = 5
A = [3, 4, 4, 6, 1, 4, 4]

print(solution(N, A))
