# Problem [5202] : 화물 도크

import sys
sys.stdin = open('input.txt')

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        D = list()
        for _ in range(N):
            s, e = map(int,input().split())
            D.append((s, e))
        D.sort(key=lambda x: x[1])
        end = D[0][0]
        cnt = 1
        for i in range(1, N):
            if end <= D[i][0]:
                end = D[i][1]
                cnt += 1
        print('#{} {}'.format(tc, cnt))