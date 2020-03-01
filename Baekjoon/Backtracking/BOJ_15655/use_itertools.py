# Problem [15655] : N과 M(6)

import sys
sys.stdin = open('input.txt')

from itertools import combinations

if __name__ == "__main__":
    N, M = map(int, input().split())
    D = sorted(list(map(int,input().split())))
    for combi in combinations(D, M):
        print(*combi)