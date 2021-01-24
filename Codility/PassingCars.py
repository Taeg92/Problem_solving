def solution(A):
    # write your code in Python 3.6
    result = 0
    east_cnt = 0

    for num in A:
        if not num:
            east_cnt += 1
        if num:
            result += east_cnt

    if result > 1000000000:
        return -1
    return result


A = [0, 1, 0, 1, 1]

print(solution(A))
