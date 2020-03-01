# Problem [15663] : N과 M(9)

import sys
sys.stdin = open('input.txt')

from itertools import permutations

if __name__ == "__main__":
    N, M = map(int, input().split())
    D = sorted(list(map(int,input().split())))
    result = list()
    for perm in permutations(D, M):
        result.append(tuple(perm))
    result = sorted(list(set(result)))
    for r in result:
        print(*r)