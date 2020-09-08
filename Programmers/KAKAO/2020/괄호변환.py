def division(p):
    cnt = [0, 0]
    for i in range(len(p)):
        if p[i] == '(':
            cnt[0] += 1
        else:
            cnt[1] += 1
        if cnt[0] == cnt[1]:
            return (p[:i+1], p[i+1:])
        

def isRight(p):
    stack = list()
    for s in p:
        if s == '(':
            stack.append(p)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return True

def solution(p):

    if not p:
        return ''
    
    u, v = division(p)

    if isRight(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for i in range(1, len(u)-1):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('
        
        return answer

p = "()))((()"
print(solution(p))