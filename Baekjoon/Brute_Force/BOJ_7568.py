# Problem [7568] : 덩치

size = int(input())
people = [list(map(int,input().split())) for _ in range(size)]
rank = [1]*size

for i in range(size):
    cnt = 1
    for j in range(size):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1
    rank[i] = cnt

print(' '.join(map(str,rank)))