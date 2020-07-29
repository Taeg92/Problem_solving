def solution(s):
    answer = True
    p_cnt = 0
    y_cnt = 0
    for ch in s:
        if ch.upper() == 'P':
            p_cnt += 1
        elif ch.upper() == 'Y':
            y_cnt += 1
    if p_cnt == y_cnt:
        return True
    else:
        return False
    
s = "pPoooyY"
print(solution(s))