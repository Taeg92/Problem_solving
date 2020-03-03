# Problem [13460] : 구슬 탈출 2

from collections import deque
import sys
sys.stdin = open('input.txt')

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def find_idx(arr):
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'R':
                rx, ry = i, j
            elif arr[i][j] == 'B':
                bx, by = i, j
    return rx, ry, bx, by

def move(x, y, dx, dy):
    cnt = 0
    while D[x+dx][y+dy] != '#' and D[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


def BFS(rx, ry, bx, by, depth):
    
    queue = deque()
    queue.append((rx, ry, bx, by, depth))
    check[rx][ry][bx][by] = 1
    # R_check[rx][ry] = 1
    # B_check[bx][by] = 1

    while queue:
        crx, cry, cbx, cby, d = queue.popleft()
        if d >= 10:
            return -1
        for i in range(4):
            nrx, nry, rcnt = move(crx, cry, dx[i], dy[i])
            nbx, nby, bcnt = move(cbx, cby, dx[i], dy[i])
            if D[nbx][nby] == 'O':
                continue
            if D[nrx][nry] == 'O':
                return d+1
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                elif rcnt < bcnt:
                    nbx -= dx[i]
                    nby -= dy[i]

            # if R_check[nrx][nry] or not B_check[nbx][nby]:
            if not check[nrx][nry][nbx][nby]:
                check[nrx][nry][nbx][nby] = 1
                queue.append((nrx,nry,nbx,nby,d+1))
    return -1
if __name__ == "__main__":
    N, M = map(int,input().split())
    D = [list(input()) for _ in range(N)]
    rx, ry, bx, by = find_idx(D)
    # R_check = [[0]*M for _ in range(N)]
    # B_check = [[0]*M for _ in range(N)]
    check = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    result = BFS(rx, ry, bx, by, 0)
    print(result)