# Problem [15654] : N과 M(5)

import sys
sys.stdin = open('input.txt')

from itertools import permutations

if __name__ == "__main__":
    N, M = map(int, input().split())
    D = sorted(list(map(int,input().split())))
    for perm in permutations(D,M):
        print(*perm)