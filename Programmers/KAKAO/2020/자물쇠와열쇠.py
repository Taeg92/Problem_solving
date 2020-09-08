def rotate(arr):
    N = len(arr)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = arr[r][c]

    return ret

def check(arr, M, N):
    for i in range(M, M+N):
        for j in range(M, M+N):
            if arr[i][j] > 1 or arr[i][j] == 0:
                return False
    return True


def drawMap(x, y, M, N, key, lock):
    ret = [[0]*(2*M+N) for _ in range(2*M+N)]

    for i in range(N):
        for j in range(N):
            ret[M+i][M+j] += lock[i][j]

    for i in range(M):
        for j in range(M):
            ret[i+y][j+x] += key[i][j]

    return ret


def solution(key, lock):

    M = len(key)
    N = len(lock)

    for _ in range(4):
        key = rotate(key)
        for i in range(0, M+N):
            for j in range(0, M+N):
                myMap = drawMap(i, j, M, N, key, lock)
                if check(myMap, M, N):
                    return True
    
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = 	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))