def solution(n, words):
    answer = [0, 0]
    answer_list = [words[0]]
    for i in range(1, len(words)):
        if words[i-1][-1] == words[i][0] and words[i] not in answer_list:
            answer_list.append(words[i])
        else:
            answer[0] = (i % n) + 1
            answer[1] = (i // n) + 1
            break
    return answer

n = 3
words = ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']
print(solution(n, words))