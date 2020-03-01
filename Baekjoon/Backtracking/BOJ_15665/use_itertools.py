# Problem [15665] : N과 M(11)

from itertools import product
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('input.txt')

if __name__ == "__main__":
    N, M = map(int,input().split())
    D = sorted(list(map(int,input().split())))
    result = list()
    for prod in product(D, repeat=M):
        result.append(prod)
    result = sorted(list(set(result)))
    for r in result:
        print(*r)
    