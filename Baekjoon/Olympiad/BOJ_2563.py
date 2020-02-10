# Problem [2563] : 색종이
# 색종이 길이 = 10

paper = [[0]*100 for _ in range(100)]
N = int(input())
cnt = 0
for _ in range(N):
    x, y = map(int,input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            if paper[i][j] == 0:
                paper[i][j] = 1

for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            cnt += 1

print(cnt)