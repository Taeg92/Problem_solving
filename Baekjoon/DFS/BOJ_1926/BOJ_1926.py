# Problme [1926] : 그림

import sys
sys.setrecursionlimit(500*500)
sys.stdin = open('input.txt')

def DFS(col,row):
    global area
    check[col][row] = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        x = col + dx[i]
        y = row + dy[i]
        if 0 <= x < N and 0 <= y < M:
            if not check[x][y] and d[x][y] == 1:
                check[x][y] = 1
                area += 1
                area_list.append(area)
                DFS(x,y)

N, M = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(N)]
check = [[0]*M for _ in range(N)]
area_list = list()
cnt = 0
m = 0
for i in range(N):
    area = 1
    for j in range(M):
        if d[i][j] == 1 and not check[i][j]:
            DFS(i,j)
            cnt += 1
    area_list.append(area)
    if max(area_list) > m:
        m = max(area_list) 
print(cnt)
print(m)
