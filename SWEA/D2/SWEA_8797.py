# Problem [8797] : 당근 수확 4

def max_sum(arr):
    N = len(arr)
    m = list()

    #1번 구역
    s = 0
    for i in range(N//2 + 1):
        for j in range(i+1, N-i-1):
            s += arr[i][j]
    m.append(s)

    #2번 구역
    s = 0
    for i in range(N//2 + 1):
        for j in range(i+1, N-i-1):
            s += arr[j][i]
    m.append(s)

    #3번 구역
    s = 0
    for i in range(N//2 + 1, N):
        for j in range(N-i, i):
            s += arr[i][j]
    m.append(s)
    
    #4번 구역
    s = 0
    for i in range(N//2 + 1, N):
        for j in range(N-i, i):
            s += arr[j][i]
    m.append(s)
    
    return max(m)-min(m)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    d = [list(map(int,input().split())) for _ in range(N)]
    m = max_sum(d)
    print('#{} {}'.format(tc,m))
