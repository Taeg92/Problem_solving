def solution(n):
    answer = 0
    flag = False
    def getCntOne(n):
        cnt = 0
        binary = bin(n)[2:]
        for i in range(len(binary)):
            if binary[i] == '1':
                cnt += 1
        return cnt
    
    one_cnt = getCntOne(n)
    print(one_cnt)

    while 1:
        n += 1

        if getCntOne(n) == one_cnt:
            flag = True
        
        if flag:
            answer = n
            break
        
    return answer


n = 78
print(solution(n))