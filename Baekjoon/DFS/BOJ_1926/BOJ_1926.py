# Problme [1926] : 그림

import sys
sys.setrecursionlimit(1000*1000)
sys.stdin = open('input.txt')


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(col,row):
    check[col][row] = 1
    ret = 1

    for i in range(4):
        x = col + dx[i]
        y = row + dy[i]
        if 0 <= x < N and 0 <= y < M:
            if not check[x][y] and d[x][y] == 1:
                ret += DFS(x,y)
    
    return ret


N, M = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(N)]
check = [[0]*M for _ in range(N)]
cnt = 0
m = 0
for i in range(N):
    for j in range(M):
        if d[i][j] == 1 and not check[i][j]:
            m = max(m, DFS(i,j))
            cnt += 1
print(cnt)
print(m)
