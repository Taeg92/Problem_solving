# Problem [3752] : 가능한 시험 점수

import sys
sys.stdin = open('input.txt')


if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        D = tuple(map(int,input().split()))
        s = sum(D)
        C = [1] + [0]*s
        for i in range(N):
            for j in range(s,-1,-1):
                if C[j]:
                    C[j+D[i]] = 1
        print('#{} {}'.format(tc, sum(C)))