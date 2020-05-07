# Problem [5201] : 컨테이너 운반

import sys
sys.stdin = open('input.txt')


if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N, M = map(int, input().split())
        C = list(map(int, input().split()))
        V = [0]*N
        T = list(map(int, input().split()))
        C.sort(reverse=True)
        T.sort(reverse=True)
        s = 0
        for i in range(M):
            for j in range(N):
                if T[i] >= C[j] and not V[j]:
                    V[j] = 1
                    s += C[j]
                    break
        print('#{} {}'.format(tc, s))