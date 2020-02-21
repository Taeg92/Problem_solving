# Problem[17070] : 파이프 옮기기 1

from collections import deque
import sys
sys.stdin = open()

dx = [0, 1, 1] 
dy = [1, 0, 1]  

def BFS(x, y, shape):
    cnt = 0
    queue = deque()
    queue.append([x, y, shape])
    while queue:
        cx, cy, s = queue.popleft()
        if cx == N-1 and cy == N-1:
            cnt += 1

        for i in range(3):
            nx = cx + dx[i] 
            ny = cy + dy[i]
            ns = i
            if nx < N and ny < N and s + ns != 1:
                if not D[nx][ny]:
                    if i == 2:
                        if not D[nx-1][ny] and not D[nx][ny-1]:
                            queue.append([nx, ny, ns])
                    else:
                        queue.append([nx, ny, ns])
    return cnt

if __name__ == "__main__":
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    print(BFS(1,0,1))