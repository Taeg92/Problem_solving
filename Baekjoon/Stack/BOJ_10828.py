# Problem [10828] : 스택
from collections import deque
import sys
input = lambda : sys.stdin.readline()


T = int(input())
arr = deque()
for _ in range(T):
    cmd, *n = input().split()
    if cmd == 'push':
        arr.append(int(n[0]))
    elif cmd == 'pop':
        if len(arr) == 0:
            print('-1')
        else:
            print(arr.pop())
    elif cmd == 'size':
        print(len(arr))
    elif cmd == 'empty':
        if len(arr) == 0:
            print('1')
        else:
            print('0')
    elif cmd == 'top':
        if len(arr) == 0:
            print('-1')
        else:
            print(arr[-1])
