# Problem [2477] : 참외밭
# 1: 동 2: 서 3: 남: 4: 북

def calc_area(data):
    max_h = 0
    max_w = 0
    min_h = 0
    min_w = 0
    maxH_idx = 0
    maxW_idx = 0
    max_area = 0
    min_area = 0

    for i in range(len(data)):
        if data[i][0] == 1 or data[i][0] == 2:
            if data[i][1] > max_w:
                max_w = data[i][1]
                maxW_idx = i
        elif data[i][0] == 3 or data[i][0] == 4:
            if data[i][1] > max_h:
                max_h = data[i][1]
                maxH_idx = i

    max_area = max_h*max_w

    if maxH_idx < 3 :
        min_w = data[maxH_idx+3][1]
    else:
        min_w = data[maxH_idx-3][1]
    
    if maxW_idx < 3 :
        min_h = data[maxW_idx+3][1]
    else:
        min_h = data[maxW_idx-3][1]
    
    min_area = min_h*min_w

    
    
    return max_area - min_area



K = int(input())
data = [list(map(int,input().split())) for _ in range(6)]
area = calc_area(data)
print(area*K)