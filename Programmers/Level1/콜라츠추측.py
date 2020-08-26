def solution(num):
    answer = 0
    cnt = 0
    while 1:
        if cnt >= 500:
            return -1
        if num == 1:
            return cnt
        if num%2:
            num = num*3 + 1
        else:
            num //= 2
        
        cnt += 1

num = 16
print(solution(num))