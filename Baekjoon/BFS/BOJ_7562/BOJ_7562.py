# Problem [7562] : 나이트의 이동

from collections import deque
import sys
sys.stdin = open('input.txt')

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def BFS(x,y,depth):
    check[x][y] = 1
    queue = deque()
    queue.append([x,y,depth])
    while queue:
        cx, cy, cd = queue.popleft()
        if cx == ec and cy == er:
            return cd
        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            nd = cd + 1
            if 0 <= nx < L and 0 <= ny < L:
                if not check[nx][ny]:
                    check[nx][ny] = 1
                    queue.append([nx,ny,nd])
        

if __name__ == "__main__":
    T = int(input())
    for tc in range(T):
        L = int(input())
        sc, sr = map(int, input().split())
        ec, er = map(int, input().split())
        check = [[0]*L for _ in range(L)]
        print(BFS(sc,sr,0))
        
