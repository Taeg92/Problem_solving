# Problem [1949] : 등산로 조정

import sys
sys.stdin = open('input.txt')

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
def DFS(x, y, d, k):
    global m
    if m < d:
        m = d
    C[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not C[nx][ny]:
            if D[x][y] <= D[nx][ny]:
                if D[x][y] > D[nx][ny] - k:
                    temp = D[nx][ny]
                    D[nx][ny] = D[x][y]-1
                    DFS(nx,ny,d+1,0)
                    D[nx][ny] = temp
            else:
                DFS(nx,ny,d+1,k)
    C[x][y] = 0

def get_Max(arr):
    m = 0
    for col in arr:
        m = max(m,max(col))
    return m
   
if __name__ == "__main__":
    T= int(input())
    for tc in range(1, T+1):
        N, K = map(int, input().split())
        D = [list(map(int, input().split())) for _ in range(N)]
        maxD = get_Max(D)
        L = [[i,j] for i in range(N) for j in range(N) if D[i][j] == maxD]
        C = [[0]*N for _ in range(N)]
        m = 0
        for axis in L:
            c, r = axis
            DFS(c,r,1,K)
        print('#{} {}'.format(tc,m))