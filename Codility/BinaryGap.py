def solution(N):
    # write your code in Python 3.6
    binary = bin(N)[2:]
    pos_list = []
    for idx, val in enumerate(binary):
        if val == '1':
            pos_list.append(idx)

    gap = [0]
    for idx in range(len(pos_list) - 1):
        gap.append(pos_list[idx + 1] - pos_list[idx] - 1)

    return max(gap)


N = 5

print(solution(5))
