def solution(s):
    answer = ''
    dev = len(s) // 2
    if len(s) % 2 :
        answer += s[dev]
    else:
        answer += s[dev-1] + s[dev]
    return answer

s = 'abcde'
print(solution(s))