def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    for num in set_reserve:
        if (num - 1) in set_lost:
            set_lost.remove(num - 1)
        elif (num + 1) in set_lost:
            set_lost.remove(num + 1)

    return n - len(set_lost)


n = 5
lost = [2, 4]
reserve = [1, 3, 5]

print(solution(n, lost, reserve))
