def solution(d, budget):
    answer = 0
    rest = budget
    d.sort()
    for price in d:
        rest -= price
        if rest < 0:
            return answer
        answer += 1
    return answer


d = [2, 2, 3, 3]
budget = 10

print(solution(d, budget))
