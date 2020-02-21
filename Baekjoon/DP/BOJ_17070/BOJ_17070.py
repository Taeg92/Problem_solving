# Problem [17070] : 파이프 옮기기 1

import sys
sys.stdin = open('input.txt')
input = lambda : sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    D = [list(map(int,input().split())) for _ in range(N)]