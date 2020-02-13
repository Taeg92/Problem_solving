# Problem [10773] : 제로

from collections import deque
import sys
input = lambda : sys.stdin.readline()

arr = deque()
T = int(input())
for _ in range(T):
    n = int(input())
    if n == 0:
        arr.pop()
    else:
        arr.append(n)
print(sum(arr))
        





