# Problem [10026] : 적록색약

from collections import deque
import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS_RGB(x,y,color):

    queue = deque()
    check_RGB[x][y] = 0
    queue.appendleft([x,y])

    while queue:

        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not check_RGB[nx][ny] and d[nx][ny] == color:
                    check_RGB[nx][ny] = 1
                    queue.append([nx,ny])

def BFS_RG(x,y,color):
    
    queue = deque()
    check_RG[x][y] = 0
    queue.appendleft([x,y])

    while queue:

        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not check_RG[nx][ny]:
                    if color == 'R':
                        if d[nx][ny] == 'R' or d[nx][ny] == 'G':
                            check_RG[nx][ny] = 1
                            queue.append([nx,ny])
                    elif color == 'G':
                        if d[nx][ny] == 'R' or d[nx][ny] == 'G':
                            check_RG[nx][ny] = 1
                            queue.append([nx,ny])
                    else:
                        if d[nx][ny] == 'B':
                            check_RG[nx][ny] = 1
                            queue.append([nx,ny])

                

if __name__ == "__main__":
    N = int(input())
    d = [list(input()) for _ in range(N)]
    check_RGB = [[0]*N for _ in range(N)]
    check_RG = [[0]*N for _ in range(N)]
    cnt = [0, 0]
    for i in range(N):
        for j in range(N):
            if not check_RGB[i][j]:
                BFS_RGB(i,j,d[i][j])
                cnt[0] += 1
            if not check_RG[i][j]:
                BFS_RG(i,j,d[i][j])
                cnt[1] += 1
            
    print(' '.join(map(str,cnt)))