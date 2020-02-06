# Problem [1211] : Ladder2

T = 10
for _ in range(1, T+1):
    tc = int(input())
    data = [list(map(int,input().split())) for _ in range(100)]
    arrive_idx = 0
    start = [i for i in range(100) if data[0][i] == 1]
    min_cnt = 10000000

    for i in start:
        cnt = 0
        j = 0
        state = i
        while 1:
            if i+1 <= 99 and data[j][i+1] == 1:
                while i+1 <= 99 and data[j][i+1] == 1:
                    i += 1
                    cnt += 1
                j += 1
            elif i-1 >=0 and data[j][i-1] == 1:
                while i-1 >=0 and data[j][i-1] == 1 :
                    i -= 1
                    cnt += 1
                j += 1
            else:
                j += 1
        
            if j == 99:
                if min_cnt >= cnt:
                    min_cnt = cnt
                    arrive_idx = state
                break
    print('#{} {}'.format(tc,arrive_idx))