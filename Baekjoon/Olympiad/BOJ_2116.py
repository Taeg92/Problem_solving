# Problem [2116] : 주사위 쌓기
# 입력 첫째 줄 : 주사위 개수
# 입력 둘째 줄 부터 1번 주사위 부터 입력받음(가장 밑에 있는 주사위)

def max_arr(arr,num):
    idx = arr.index(num)
    if idx in [0,5]:
        temp = [arr[i] for i in range(len(arr)) if i != 0 and i != 5]
        return max(temp)
    elif idx in [1,3]:
        temp = [arr[i] for i in range(len(arr)) if i != 1 and i != 3]
        return max(temp)
    elif idx in [2,4]:
        temp = [arr[i] for i in range(len(arr)) if i != 2 and i != 4]
        return max(temp) 

def couple(arr,num):
    idx = arr.index(num)
    if idx == 0:
        return arr[5]
    elif idx == 1:
        return arr[3]
    elif idx == 2:
        return arr[4]
    elif idx == 3:
        return arr[1]
    elif idx == 4:
        return arr[2]
    else:
        return arr[0]

            

# 주사위 개수
N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
m = 0
for i in range(6):
    s = 0
    prev = data[0][i]
    for j in range(N):
        num = couple(data[j],prev)
        s += max_arr(data[j],num)
        prev = num
    if m < s:
        m = s
print(m)