# Problem [15664] : N과 M(10)

from itertools import combinations
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('input.txt')

if __name__ == "__main__":
    N, M = map(int,input().split())
    D = sorted(list(map(int,input().split())))
    result = list()
    for combi in combinations(D,M):
        result.append(tuple(combi))
    result = sorted(list(set(result)))
    for r in result:
        print(*r)