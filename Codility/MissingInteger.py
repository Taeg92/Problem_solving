def solution(A):
    # write your code in Python 3.6
    data = set(range(1, 1000001))
    return min(data - set(A))


A = [1, 3, 6, 4, 1, 2]

print(solution(A))
