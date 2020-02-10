# Problem [2491] : 수열

N = int(input())
data = list(map(int,input().split()))

up = 1
down = 1
max_up = 0
max_down = 0
result = 0
for i in range(len(data)-1):
    if data[i] < data[i+1]:
        up += 1
        if down > max_down:
            max_down = down
        down = 1
    elif data[i] > data[i+1]:
        down += 1
        if up > max_up:
            max_up = up
        up = 1
    else:
        up += 1
        down += 1
if up > max_up:
    max_up = up
if down > max_down:
    max_down = down

if max_up > max_down:
    result = max_up
elif max_down > max_up:
    result = max_down
else:
    result = max_up

print(result)