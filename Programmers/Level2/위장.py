from collections import Counter


def solution(clothes):
    category_cnt = Counter([kind for _, kind in clothes])

    number_of_cases = 1
    for kind in category_cnt:
        number_of_cases *= category_cnt[kind] + 1

    return number_of_cases - 1


clothes = [
    ["yellowhat", "headgear"],
    ["bluesunglasses", "eyewear"],
    ["green_turban", "headgear"]
]

print(solution(clothes))
