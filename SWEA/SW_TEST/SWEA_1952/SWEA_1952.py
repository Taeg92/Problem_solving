# Problem [1952] : [모의 SW 역량 테스트] 수영장

import sys
sys.stdin = open('input.txt')

def DFS(n,v):
    global m
    if n > 12:
        m = min(m, v)
        return
    if P[n] == 0:
        DFS(n+1,v)
        return
    else:
        DFS(n+1, v + P[n]*C[0])
        DFS(n+1, v + C[1])
        DFS(n+3, v + C[2])


if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        C = list(map(int,input().split()))
        P = [0] + list(map(int,input().split()))
        m = C[3]
        DFS(1,0)
        print('#{} {}'.format(tc,m))