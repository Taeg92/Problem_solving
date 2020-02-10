# Problem [10163] : 색종이

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]

arr = [[0]*101 for _ in range(101)]
color = 0
cnt = [0]*101
result = list()
for d in data:
    color += 1
    for i in range(d[1],d[1]+d[3]):
        for j in range(d[0],d[0]+d[2]):
            arr[i][j] = color

for i in range(len(arr)):
    for j in range(len(arr[0])):
        cnt[arr[i][j]] += 1



for i in range(1,N+1):
    print(cnt[i])