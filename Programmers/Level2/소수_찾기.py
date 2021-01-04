from itertools import permutations


def check(num_set):
    for i in range(2, int(max(num_set) ** 0.5) + 1):
        num_set -= set(range(i * 2, max(num_set) + 1, i))
    return len(num_set)


def solution(numbers):
    answer = 0
    num_set = set()
    for i in range(len(numbers)):
        num_set |= set(
            map(int, map(''.join, permutations(list(numbers), i + 1))))
    num_set -= set(range(0, 2))

    return check(num_set)


numbers = "011"

print(solution(numbers))
