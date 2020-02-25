#Problem [17471] : 게리맨더링

import sys
input = lambda : sys.stdin.readline().rstrip()
sys.stdin = open('input.txt')


if __name__ == "__main__":
    N = int(input())
    D = list(map(int,input().split()))