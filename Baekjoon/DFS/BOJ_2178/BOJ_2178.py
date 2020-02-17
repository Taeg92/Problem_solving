# Problem [2178] : 미로 탐색

import sys
sys.stdin = open('input.txt')

def DFS(u,v,dist):

    check[u][v] = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dt = 1
    if u == N and v == M:
        result.append(dist)

    for i in range(4):
        x = u + dx[i]
        y = v + dy[i]
        d = dist + dt
        if (1 <= x <= N) and (1 <= y <= M):
            if not check[x][y] and data[x-1][y-1] == 1:
                check[x][y] = 1
                DFS(x,y,d)
                check[x][y] = 0


N, M = map(int,input().split())
data = [list(map(int,list(input()))) for _ in range(N)]
check = [[0]*(M+1) for _ in range(N+1)]
result = list()
DFS(1,1,1)
print(min(result))