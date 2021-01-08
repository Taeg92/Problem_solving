# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import deque


def solution(A, K):
    if not A:
        return A

    dq = deque(A)

    for _ in range(K):
        dq.appendleft(dq.pop())
    return list(dq)


A = [3, 8, 9, 7, 6]
K = 3

print(solution(A, K))
