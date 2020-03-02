# Problem [1953] : 탈주범 검거

import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
shape = [[], [0, 1, 2, 3], [0, 2], [1, 3], [0, 1], [1, 2], [2, 3], [0, 3]]  


def DFS(x, y, d, s):
    if d <= L:
        result.add((x,y))
    else:
        return 
    for i in range(len(shape[s])):
        nx = x + dx[shape[s][i]]
        ny = y + dy[shape[s][i]]
        if 0 <= nx < N and 0 <= ny < M and not check[nx][ny]:
            if [x-nx, y-ny] in [[dx[k],dy[k]] for k in shape[D[nx][ny]]]:
                check[nx][ny] = 1
                DFS(nx, ny, d+1, D[nx][ny])
                check[nx][ny] = 0

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N, M, R, C, L = map(int,input().split())
        D = [list(map(int,input().split())) for _ in range(N)]
        check = [[0]*M for _ in range(N)]
        result = set()
        DFS(R, C, 1, D[R][C])
        print('#{} {}'.format(tc,len(result)))