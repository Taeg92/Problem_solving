# Problem [17070] : 파이프 옮기기 1
# 시간 초과 
import sys
sys.stdin = open('input.txt')
input = lambda : sys.stdin.readline().rstrip()


result = 0
def DFS(x,y,shape):
    global result

    if x == N-1 and y == N-1:
        result += 1

    if shape == 'd' or shape == 'w' or shape == 'h':
        if 0 <= x+1 < N and 0 <= y+1 < N:
            if not D[x+1][y+1] and not D[x+1][y] and not D[x][y+1]:
                DFS(x+1,y+1,'d')

    if shape == 'd' or shape == 'h':
        if 0 <= x+1 < N and 0 <= y < N:
            if not D[x+1][y]:
                DFS(x+1,y,'h')
    if shape == 'd' or shape == 'w':
        if 0 <= x < N and 0 <= y+1 < N:
            if not D[x][y+1]:
                DFS(x,y+1,'w')

if __name__ == "__main__":
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    DFS(0,1,'w')
    print(result)