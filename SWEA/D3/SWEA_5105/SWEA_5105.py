# Problem [5105] : 미로의 거리
import sys
sys.stdin = open('input.txt')


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def BFS(x,y, depth):
    C[x][y] = 1
    Q = list()
    Q.append((x,y,depth))

    while Q:
        cx, cy, d = Q.pop(0)
        if D[cx][cy] == 3:
            return d-1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not C[nx][ny] and D[nx][ny] in [0,3]:
                    C[nx][ny] = 1
                    Q.append((nx,ny,d+1))
    return 0

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        D = [list(map(int,list(input()))) for _ in range(N)]
        C = [[0]*N for _ in range(N)]
        S = [(i,j) for i in range(N) for j in range(N) if D[i][j] == 2]
        result = BFS(S[0][0], S[0][1], 0)
        print(f'#{tc} {result}')