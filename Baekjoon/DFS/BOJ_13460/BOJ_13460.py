# Problem [13460] : 구슬 탈출 2

import sys
sys.stdin = open('input.txt')


if __name__ == "__main__":
    N, M = map(int,input().split())
    D = [list(input()) for _ in range(N)]
    print(D)