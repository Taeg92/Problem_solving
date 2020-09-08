def solution(s):

    answer = list()

    if len(s) == 1:
        return 1
    
    for unit in range(1, len(s)//2 + 1):

        cnt = 1
        cut = s[:unit]
        temp = ''

        for i in range(unit, len(s), unit):
            word = s[i:i+unit]
            if cut == word:
                cnt += 1
            else:
                if cnt == 1:
                    temp += cut
                else:
                    temp += str(cnt) + cut
                cut = word
                cnt = 1
        if cnt == 1:
            temp += cut
        else:
            temp += str(cnt) + cut
        
        answer.append(len(temp))

    return min(answer)

s = "ababcdcdababcdcd"
print(solution(s))