# Problem [1697] : 숨바꼭질
# 시간 초과 => N이 너무 커서 백트래킹 불가

import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10000000)

def BT(n,depth):
    global result
    check[n] = 1
    if n == M:
        result.append(depth)
    n1 = n - 1
    n2 = n + 1
    n3 = n*2

    if 0 <= n1 <= M+1 and not check[n1]:
        check[n1] = 1
        BT(n1,depth+1)
        check[n1] = 0
    if 0 <= n2 <= M+1 and not check[n2]:
        check[n2] = 1
        BT(n2,depth+1)
        check[n2] = 0 
    if 0 <= n3 <= M+1 and not check[n3]:
        check[n3] = 1
        BT(n3,depth+1)
        check[n3] = 0

if __name__ == "__main__":
    N, M = map(int,input().split())
    check = [0]*max(N+1,M+2)
    result = list()
    isPossible = 0
    if N > M:
        print(N-M)
    else:
        BT(N,0)
        print(min(result))