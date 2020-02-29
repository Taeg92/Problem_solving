# Problem [17472] : 다리 만들기 2

from collections import deque
from itertools import combinations
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

m = float('inf')

# 구역 나누기
def DFS(x,y,n):
    D[x][y] = n
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not C[nx][ny]:
            if D[nx][ny]:
                C[nx][ny] = 1
                D[nx][ny] = n
                DFS(nx,ny,n)
            else:
                E[x][y] = 1

def Cost(x,y):
    pos = D[x][y]
    for i in range(4):
        cnt = 0
        cx = x
        cy = y 
        while 1:
            cx = cx + dx[i]
            cy = cy + dy[i]
            if 0 <= cx < N and 0 <= cy < M and not D[cx][cy]:
                cnt += 1
            else:
                break
        if 0 <= cx < N and 0 <= cy < M and D[cx][cy] != pos and cnt >= 2:
            npos = D[cx][cy]
            P[pos][npos] = P[npos][pos] = min(cnt,P[pos][npos])


def connect(n, v):
    global m
    if n == size:
        if sum(check) == section-1:
            if BFS(1,0):
                m = min(m,v)
                return
            else:
                return
        else:
            return

    cost, land1, land2 = data[n] 
    if not visited[n]:
        visited[n] = 1
        check[land1] = 1
        check[land2] = 1
        connect(n+1,v+cost)

def BFS(x,depth):
    V = [0]*(section)
    V[x] = 1
    queue = deque()
    queue.append(x)

    while queue:
        q = queue.popleft()
        for w in Graph[q]:
            if not V[w]:
                V[w] = 1
                queue.append(w)
    
    if sum(V) == section-1:
        return True
    return False


if __name__ == "__main__":
    N, M = map(int,input().split())
    D = [list(map(int,input().split())) for _ in range(N)]
    C = [[0]*M for _ in range(N)]
    E = [[0]*M for _ in range(N)]
    Possible = True
    result = 0
    
    # 구역 나누기
    section = 1
    for i in range(N):
        for j in range(M):
            if D[i][j] and not C[i][j]:
                DFS(i,j,section)
                section += 1

    # 최소 다리 비용, 연결 확인
    P = [[float('inf')]*section for _ in range(section)]
    for i in range(N):
        for j in range(M):
            if E[i][j]:
                Cost(i,j)

    # 조합으로 비용 무한대를 제외하고 섬 두개 선택
    array = list()
    for combi in combinations(range(1,section),2):
        x, y = combi
        if P[x][y] != float('inf'):
            array.append([P[x][y],x,y])

    if not array:
        Possible = False
    else:
        combi_array = list()
        size = section-2
        for combi in combinations(array,size):
            Graph = [[] for _ in range(section)]
            for location in combi:
                val, u, v = location
                Graph[u].append(v)
                Graph[v].append(u)
            visited = [0]*len(array)
            check = [0]*section
            data = list(combi)
            connect(0,0)
    if Possible:
        if m == float('inf'):
            print(-1)
        else:
            print(m)
    else:
        print(-1)