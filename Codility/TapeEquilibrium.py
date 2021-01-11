import sys


def solution(A):
    # write your code in Python 3.6
    right_sum = sum(A)
    left_sum = 0
    diff = sys.maxsize

    for i in range(len(A) - 1):
        right_sum -= A[i]
        left_sum += A[i]

        diff = min(diff, abs(right_sum - left_sum))

    return diff


A = [3, 1, 2, 4, 3]

print(solution(A))
