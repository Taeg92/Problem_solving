# Problem [17135] : 캐슬 디펜스

import sys
sys.stdin = open('input.txt')

if __name__ == "__main__":
    N, M, D = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)] + [[0]*N]
    print(data)
