# Problem [13460] : 구슬 탈출 2

import sys
sys.stdin = open('input.txt')

def DFS(x,y):
    return

if __name__ == "__main__":
    N, M = map(int,input().split())
    D = [list(input()) for _ in range(N)]
    A = [[i,j] for i in range(N) for j in range(M) if D[i][j] == 'R' or D[i][j] == 'B' or D[i][j] == 'O']
    print(A)