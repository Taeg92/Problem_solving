# Problem [2651] : 자동차경주대회
# 시간 초과
import sys
from collections import deque
sys.stdin = open('input.txt')
input = lambda: sys.stdin.readline().rstrip()

m = sys.maxsize

def DFS(v,t):
    global m
    if t > m:
        return
    if v == N+1:
        if  m > t:
            m = t
            result.append(check[:])
        return
    for i in range(N+2):
        if not check[i] and data[i] - data[v] <= dist:
            check[i] = 1
            DFS(i,t+T[i])
            check[i] = 0

if __name__ == '__main__':
    dist = int(input())
    N = int(input())
    data = deque(list(map(int, input().split())))
    T = deque(list(map(int, input().split())))
    result = list()
    time = list()
    check = [0]*(N+2)

    T.append(0)
    T.appendleft(0)

    for i in range(1,len(data)):
        data[i] += data[i-1]
    data.appendleft(0)

    
    DFS(0,0)

    for r in result:
        s = 0
        for i in range(1,N+1):
            if r[i]:
                s += T[i]
        if s == m:
            time = r

    result = list()
    cnt = 0
    for i in range(1,N+1):
        if time[i]:
            cnt += 1
            result.append(i)

    print(m)
    print(cnt)
    print(*result)