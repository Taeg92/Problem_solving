def get_ternary(n):
    ret = ""

    while n > 0:
        n, r = divmod(n, 3)
        ret += str(r)

    return ret


def solution(n):
    return int(get_ternary(n), 3)


n = 45
print(solution(n))
