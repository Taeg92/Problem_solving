# Problem [5207] : 이진 탐색

import sys
sys.stdin = open('input.txt')

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N, M = map(int, input().split())
        nArray = sorted(list(map(int,input().split())))
        mArray = list(map(int, input().split()))

        cnt = 0
        for n in mArray:
            start = 0
            end = N-1

            flag = 0
            while start <= end:
                mid = (start + end) // 2

                if n >= nArray[mid]:
                    if n == nArray[mid]:
                        cnt += 1
                        break

                    start = mid + 1
                    if flag == 1: 
                        break
                    flag = 1

                elif n < nArray[mid]:
                    end = mid - 1
                    if flag == -1: 
                        break
                    flag = -1

        print('#{} {}'.format(T, cnt))