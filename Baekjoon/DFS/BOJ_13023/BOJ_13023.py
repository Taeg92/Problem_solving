# Problem [13023] : ABCDE

import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    G = [[] for _ in range(V)]
    result = list()
    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    check = [0]*V
    print(G)
    