# Problem [1697] : 숨바꼭질

from collections import deque
import sys
sys.stdin = open('input.txt')

def BFS(n,depth):
    check[n] = 1
    queue = deque()
    queue.append([n,depth])

    while queue:

        q, d = queue.popleft()
        if q == M:
            return d
        q1 = 2*q
        q2 = q + 1
        q3 = q - 1
        if 0 <= q1 <= M+1 and not check[q1]:
            check[q1] = 1
            queue.append([q1,d+1])
        if 0 <= q2 <= M+1 and not check[q2]:
            check[q2] = 1
            queue.append([q2,d+1])
        if 0 <= q3 <= M+1 and not check[q3]:
            check[q3] = 1
            queue.append([q3,d+1])
    

if __name__ == "__main__":
    N, M = map(int,input().split())
    check = [0]*max(N+2,M+2)
    if N > M:
        print(N-M)
    else:
        print(BFS(N,0))