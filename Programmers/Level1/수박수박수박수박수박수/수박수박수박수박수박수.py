def solution(n):
    q, r = divmod(n, 2)
    return '수박' * q + '수' * r


n = 3

print(solution(n))
