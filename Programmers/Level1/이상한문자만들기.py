def solution(s):
    answer = []
    words = s.split(' ')
    for word in words:
        temp = ''
        for i in range(len(word)):
            if i % 2:
                temp += word[i].lower()
            else:
                temp += word[i].upper()
        answer.append(temp)
    return ' '.join(answer)

s = "try hello world"
print(solution(s))