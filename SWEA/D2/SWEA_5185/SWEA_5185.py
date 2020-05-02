# Problem [5185] : 이진수

import sys
sys.stdin = open('input.txt')

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N, V = input().split()
        val = int(V, 16)
        size = int(N)*4
        D = [0]*size
        idx = size-1
        while val > 0:
            D[idx] = val % 2
            idx -= 1
            val //= 2
        print('#{} {}'.format(tc, ''.join(map(str,D))))