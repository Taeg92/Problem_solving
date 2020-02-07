# Problem [2304] : 창고 다각형
# 첫째 줄 : 정수 N => 기둥의 개수
# 둘째 줄 부터 기둥의 위치와 높이

def cal_Area(data):
    max_list = find_max(data)  
    s =0
    h = 0
    start = 0 
    end = 0
    for i in range(min(max_list)+1):
        if data[i][1] > h:
            end = data[i][0]
            s += h*(end-start)
            h = data[i][1]
            start = data[i][0]

    h = 0
    start = 0
    end = 0
    for i in range(len(data)-1,max(max_list)-1,-1):
        if data[i][1] > h:
            end = data[i][0] + 1
            s += h*(start-end)
            h = data[i][1]
            start = data[i][0] + 1

    s += data[min(max_list)][1]*(data[max(max_list)][0]-data[min(max_list)][0]+1)

    return s

def find_max(data):
    m = 0
    for i in range(len(data)):
        if data[i][1] >= m:
            m = data[i][1]
    idx = [i for i in range(len(data)) if data[i][1] == m]
    return idx

N = int(input())
data = sorted([list(map(int,input().split())) for _ in range(N)])

result = cal_Area(data)
print(result)


