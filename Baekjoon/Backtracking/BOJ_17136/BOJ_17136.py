# Problem [17136] : 색종이 붙이기

import sys
sys.stdin = open('input.txt')


if __name__ == "__main__":
    D = [list(map(int,input().split())) for _ in range(10)]
    axis = [[i,j] for i in range(10) for j in range(10) if D[i][j] == 1]
    print(axis)