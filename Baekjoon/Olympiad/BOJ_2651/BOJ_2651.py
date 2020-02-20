# Problem [2651] : 자동차경주대회

import sys
sys.stdin = open('input.txt')
m = sys.maxsize
def DFS(v,d,t):
    global m
    if v == N:
        m = min(m,t)
        
    for i in range(v,N):
        if not check[i]:
            if d > data[i]:
                DFS(v+1,d - data[i],t + T[i])
            else:
                DFS(v-1,dist,t)
                check[i] = 1


if __name__ == '__main__':
    dist = int(input())
    N = int(input())
    data = list(map(int, input().split()))
    T = list(map(int, input().split()))
    check = [0]*N
    DFS(0,0,0)
    print(m)