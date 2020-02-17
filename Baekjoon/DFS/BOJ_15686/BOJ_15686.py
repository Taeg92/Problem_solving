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

home = [[i,j] for i in range(N) for j in range(N) if data[i][j] == 1]
chicken = [[i,j] for i in range(N) for j in range(N) if data[i][j] == 2]
choice_chicken = list(combination(chicken,M))
min_dist = 0
for choice in choice_chicken:
    dist = 0
    for i in range(M):
        for j in range(len(home)):
            dist += abs(choice[i][0]-home[j][0]) +abs(choice[i][1]-home[j][1])
    if min_dist == 0:
        min_dist = dist
    else:
        if min_dist > dist:
            min_dist = dist
print(min_dist)