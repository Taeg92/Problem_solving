# Problem [2564] : 경비원
# 1 => 북  ,  2 => 남  ,  3 =>  서 , 4 => 동

w, h = map(int,input().split())
N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
pos, dist = map(int,input().split())
result = list()
for d in data:
    if d[0] == 1:
        if pos == 1:
            result.append(abs(d[1]-dist))
        elif pos == 2:
            result.append(min(dist+h+d[1],(w-dist)+h+(w-d[1])))
        elif pos == 3:
            result.append(dist+d[1])
        else:
            result.append(dist+(w-d[1]))

    elif d[0] == 2:
        if pos == 1:
            result.append(min(dist+h+d[1],(w-dist)+h+(w-d[1])))
        elif pos == 2:
            result.append(abs(d[1]-dist))
        elif pos == 3:
            result.append((h-dist)+d[1])
        else:
            result.append((h-dist)+(w-d[1]))
    elif d[0] == 3:
        if pos == 1:
            result.append(dist+d[1])
        elif pos == 2:
            result.append(dist+(h-d[1]))
        elif pos == 3:
            result.append(abs(d[1]-dist))
        else:
            result.append(min(dist+w+d[1],(h-dist)+w+(h-d[1])))
    else:
        if pos == 1:
            result.append((w-dist)+d[1])
        elif pos == 2:
            result.append((w-dist)+(h-d[1]))
        elif pos == 3:
            result.append(min(dist+h+d[1],(h-dist)+w+(h-d[1])))
        else:
            result.append(abs(d[1]-dist))

print(sum(result))
    
