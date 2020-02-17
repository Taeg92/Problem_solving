# Problem [15686] : 치킨 배달

import sys
sys.stdin = open('input.txt')

def combination(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combination(arr[i+1:],r-1):
                yield [arr[i]] + next

N, M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]

home = [[i+1,j+1] for i in range(N) for j in range(N) if data[i][j] == 1]
chicken = [[i+1,j+1] for i in range(N) for j in range(N) if data[i][j] == 2]
choice_chicken = list(combination(chicken,M))
min_s = 0
for choice in choice_chicken:
    s = 0
    for i in range(len(home)):
        dist = list()
        for j in range(M):
            dist.append(abs(choice[j][0]-home[i][0]) +abs(choice[j][1]-home[i][1]))
        s += min(dist)
    if min_s == 0:
        min_s = s
    else:
        if min_s > s:
            min_s = s
print(min_s)