from collections import defaultdict


def solution(A):
    # write your code in Python 3.6
    cnt_dict = defaultdict(int)

    for idx, val in enumerate(A):
        cnt_dict[val] += 1

        if cnt_dict[val] > len(A) / 2:
            return idx

    return -1


A = [3, 4, 3, 2, 3, -1, 3, 3]

print(solution(A))
