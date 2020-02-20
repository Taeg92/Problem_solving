# Problem [2651] : 자동차경주대회

import sys
# sys.stdin = open('input.txt')
m = sys.maxsize
def DFS(v,d,t):
    global m
    if d < 0 :
        return
    if v == N:
        m = min(m,t)
    for i in range(v,N):

        if not check[i]:
            check[i] = 1
            DFS(i+1,dist,t+T[i])
            check[i] = 0

if __name__ == '__main__':
    dist = int(input())
    N = int(input())
    data = list(map(int, input().split()))
    T = list(map(int, input().split()))
    check = [0]*N
    DFS(0,dist,0)
    print(m)