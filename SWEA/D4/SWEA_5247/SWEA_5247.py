# Problem [5247] : 연산

import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(v, depth):
    C[v] = 1
    Q = deque()
    Q.append((v, depth))

    while Q:
        q, d = Q.popleft()
        if q == M:
            return d
        q1 = q+1
        q2 = q-1
        q3 = q*2
        q4 = q-10

        if 0 <= q1 <= M+10:
            if not C[q1]:
                C[q1] = 1
                Q.append((q1, d+1))
        if 0 <= q2 <= M+10:
            if not C[q2]:
                C[q2] = 1
                Q.append((q2, d+1))
        if 0 <= q3 <= M+10:
            if not C[q3]:
                C[q3] = 1
                Q.append((q3, d+1))
        if 0 <= q4 <= M+10:
            if not C[q4]:
                C[q4] = 1
                Q.append((q4, d+1))

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N, M = map(int, input().split())
        C = [0]*(2*M+20)
        result = BFS(N, 0)
        print('#{} {}'.format(tc, result))