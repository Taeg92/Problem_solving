def solution(name):
    answer = 0
    min_move = len(name) - 1
    nxt = 0

    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        nxt = i + 1
        while nxt < len(name) and name[nxt] == 'A':
            nxt += 1

        min_move = min(min_move, i + i + len(name) - nxt)

    answer += min_move

    return answer


name = "JEROEN"

print(solution(name))
