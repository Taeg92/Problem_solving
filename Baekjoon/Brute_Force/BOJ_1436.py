# Problem [1436] : 영화감독 숌
# 666이 들어간 영화 제목 만들기.

n_val = int(input())
cnt = 0
n = 1
while 1:
    end = '666'
    if end in str(n):
        cnt += 1
    if cnt == n_val :
        break
    n += 1
    
print(n)