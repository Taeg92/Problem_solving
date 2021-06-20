def solution(brown, yellow):
    answer = []

    for yellow_y in range(1, int(yellow**(0.5)) + 1):
        if not (yellow % yellow_y):
            yellow_x = yellow // yellow_y

            if (2 * yellow_x) + (2 * yellow_y) + 4 == brown:
                answer = [yellow_x + 2, yellow_y + 2]

    return answer

brown = 24
yellow = 24

print(solution(brown, yellow))