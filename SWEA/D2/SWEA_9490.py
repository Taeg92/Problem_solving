# Problem [9490] : 풍선팡

def cnt_flower(arr,i,j):
    A = arr[i][j]
    sum = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for n in range(1,A+1):
        for k in range(4):
            x = i + dx[k]*n 
            y = j + dy[k]*n
            if x < 0 or x > N-1 or y < 0 or y > M-1:
                pass
            else:
                sum += arr[x][y]
                
    sum += arr[i][j]
    return sum

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    d = [list(map(int,input().split())) for _ in range(N)]
    m = 0
    for i in range(N):
        s = 0
        for j in range(M):
            s = cnt_flower(d,i,j)
            if s > m:
                m = s
    print('#{} {}'.format(tc, m))



