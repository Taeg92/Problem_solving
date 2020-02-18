# Problme [1926] : 그림

import sys
from collections import deque 
sys.stdin = open('input.txt')


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x,y):
    check[x][y] = 1
    queue = deque()
    queue.append([x,y])
    size = 1
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not check[nx][ny] and d[nx][ny] == 1:
                    check[nx][ny] = 1
                    size += 1
                    queue.append([nx,ny])
                    
    return size
                    

if __name__ ==  "__main__":

    N, M = map(int,input().split())
    d = [list(map(int,input().split())) for _ in range(N)]
    check = [[0]*M for _ in range(N)]
    cnt = 0
    m = 0
    for i in range(N):
        for j in range(M):
            if d[i][j] == 1 and not check[i][j]:
                m = max(m, BFS(i,j))
                cnt += 1
    print(cnt)
    print(m)