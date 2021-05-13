def solution(s):
    answer = s.split(' ')
    for i in range(len(answer)):
        answer[i] = answer[i].lower().capitalize()
    return ' '.join(answer)


s = "3people unFollowed me"

print(solution(s))
