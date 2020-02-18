# Problem [2667] : 단지번호붙이기

from collections import deque
import sys
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
            if 0 <= nx < N and 0 <= ny < N:
                if not check[nx][ny] and d[nx][ny] == 1:
                    check[nx][ny] = 1
                    queue.append([nx,ny])
                    size += 1
    return size


if __name__ == "__main__":
    N = int(input())
    d = [list(map(int,list(input()))) for _ in range(N)]
    check = [[0]*N for _ in range(N)]
    result = list()

    for i in range(N):
        for j in range(N):
            if not check[i][j] and d[i][j] == 1:
                result.append(BFS(i,j))
    
    result.sort()
    size = len(result)
    print(size)
    for r in result:
        print(r)
