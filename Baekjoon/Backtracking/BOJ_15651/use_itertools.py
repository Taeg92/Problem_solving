# Problem [15651] : N과 M(3)

from itertools import product
import sys
sys.stdin = open('input.txt')

if __name__ == "__main__":
    N, M = map(int,input().split())
    for prod in product(range(1, N+1), repeat=M):
        print(*prod)