# Problem [5203] : 베이비진 게임

import sys
sys.stdin = open('input.txt')

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        D = list(map(int, input().split()))
        A = [0]*10
        B = [0]*10
        result = 0
        flag = 0
        for i in range(6):
            a, b = D[2*i], D[2*i+1]
            A[a] += 1
            if i >= 3:
                for i in range(0, 8):
                    if A[i] >= 1 and A[i+1] >= 1 and A[i+2] >= 1 or max(A) >= 3 and not flag:
                        result = 1
                        flag = 1
                        break
            B[b] += 1
            if i >= 3:
                for i in range(0, 8):
                    if B[i] >= 1 and B[i+1] >= 1 and B[i+2] >= 1 or max(B) >= 3 and not flag:
                        result = 2
                        flag = 1
                        break
            if flag:
                break
        print('#{} {}'.format(tc, result))