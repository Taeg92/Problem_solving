# Problem [17406] : 배열 돌리기 4

from itertools import permutations
from copy import deepcopy
import sys
sys.stdin = open('input.txt')

input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
D = [list(map(int, input().split())) for _ in range(K)]

result = sys.maxsize

for perm in permutations(D):
    Array = deepcopy(A)
    for r, c, s in perm:
        for rad in range(1, 1 + s):

            x, y = r - 1 - rad, c - 1 - rad
            temp = Array[x][y]
            
            for _ in range(2*rad):  
                y += 1
                Array[x][y], temp = temp, Array[x][y]
            for _ in range(2*rad):  
                x += 1
                Array[x][y], temp = temp, Array[x][y]
            for _ in range(2*rad):  
                y -= 1
                Array[x][y], temp = temp, Array[x][y]
            for _ in range(2*rad):  
                x -= 1
                Array[x][y], temp = temp, Array[x][y]

    for col in Array:
        m = sum(col)
        if m < result:
            result = m
            
print(result)