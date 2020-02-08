# Problem [9476] : 우주선 착륙

T = int(input())

def landing(arr,i,j):
    result = list()
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    for dt in range(8):
        x = i + dx[dt]
        y = j + dy[dt]
        result.append(arr[x][y])
    if max(result)-min(result) > K:
        return False
    if min(result) > arr[i][j] or arr[i][j] - min(result) > H:
        return False

    return True


for tc in range(1, T+1):
    N, M, K, H = map(int,input().split())
    d = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(1,N-1):
        for j in range(1,M-1):
            if landing(d,i,j):
                cnt += 1
    print('#{} {}'.format(tc,cnt))
