# Problem [17472] : 다리 만들기 2

import sys
input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


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

def Prim(n):

    V = [0] * n
    K = [float('inf')] * n
    K[1] = 0
    R = 0
    for _ in range(1, n):
        m_key = float('inf')

        for i in range(1, n):
            if not V[i] and K[i] < m_key:
                m_key = K[i]
                m_pos = i

        V[m_pos] = 1
        R += m_key

        for i in range(1, n):
            if not V[i] and P[m_pos][i] < K[i]:
                K[i] = P[m_pos][i]
    
    return R


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
    
    # 연결 안된 다리 있으면 불가능
    for i in range(1, section):
        if P[i] == float('inf'):
            Possible = False
            break

    if Possible:
        result = Prim(section)
        if result == float('inf'):
            print(-1)
        else:
            print(result)
    else:
        print(-1)