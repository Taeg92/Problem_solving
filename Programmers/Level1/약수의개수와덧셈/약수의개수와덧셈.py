def get_divisor_cnt(num):
    ret = []
    for i in range(1, int(num ** 0.5) + 1):
        if not num % i:
            ret.append(i)
            ret.append(num // i)

    return len(ret) if num % num**0.5 else len(ret) + 1


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = get_divisor_cnt(i)
        answer = answer - i if cnt % 2 else answer + i
    return answer


left = 13
right = 17
print(solution(left, right))
