def solution(N):
    # write your code in Python 3.6
    factor = 1
    cnt = 0
    while factor ** 2 <= N:
        if factor ** 2 == N:
            cnt += 1
        elif not N % factor:
            cnt += 2
        factor += 1

    return cnt


N = 24

print(solution(N))
