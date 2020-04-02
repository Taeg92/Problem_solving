# Problem [5097] : 6일차 회전

import sys
sys.stdin = open('input.txt')

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N, M = map(int,input().split())
        D = list(map(int,input().split()))
        for _ in range(M):
            D.append(D.pop(0))
        print(f'#{tc} {D[0]}')