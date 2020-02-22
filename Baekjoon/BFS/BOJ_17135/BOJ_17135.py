# Problem [17135] : 캐슬 디펜스

from copy import deepcopy as copy
from itertools import combinations as combi
from collections import deque
import sys
sys.stdin = open('input.txt')

m = -sys.maxsize

dx = [0, -1, 0]
dy = [-1, 0, 1]
def BFS(x,y,Range):
    check = [[0]*M for _ in range(N)]
    queue = deque()
    queue.append([x,y,Range])

    while queue:
        cx, cy, r = queue.popleft()
        if d[cx][cy]:
            dead.add((cx,cy))
            break

        for i in range(3):
            nx = cx + dx[i] 
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not check[nx][ny]:
                if r < D:
                    check[nx][ny] = 1
                    queue.append([nx,ny,r+1])
                
if __name__ == "__main__":
    N, M, D = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)] + [[0]*M]
    for axis in list(combi(range(M),3)):
        kill = 0
        d = copy(data)
        for i in range(N):
            dead = set()
            for pos in axis:
                BFS(N-i,pos,0)
            kill += len(dead)
            for col, row in dead:
                d[col][row] = 0
            d.pop(-2)
        m = max(m,kill)
    print(m)