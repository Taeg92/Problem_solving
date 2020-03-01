# Problem [15649] : N과 M(1)

from itertools import permutations
import sys
sys.stdin = open('input.txt')

if __name__ == "__main__":
    N, M = map(int,input().split())
    for perm in permutations(range(1,N+1), M):
        print(*perm)