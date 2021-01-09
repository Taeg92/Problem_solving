import math


def solution(X, Y, D):
    return math.ceil((Y - X) / D)


X, Y, D = 10, 85, 30

print(solution(X, Y, D))
