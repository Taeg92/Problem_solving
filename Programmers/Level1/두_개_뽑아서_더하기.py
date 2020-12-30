from itertools import combinations


def solution(numbers):
    answer = set()
    for comb in combinations(numbers, 2):
        answer.add(sum(comb))
    return sorted(answer)


numbers = [2, 1, 3, 4, 1]

print(solution(numbers))
