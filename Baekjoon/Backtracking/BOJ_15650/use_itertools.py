# Problem [15650] : N과 M(2)

import sys
sys.stdin = open('input.txt')

from itertools import combinations

if __name__ == "__main__":  
    N, M = map(int, input().split())
    for combi in combinations(range(1, N+1), M):
        print(*combi)