# Problem [2635] : 수 이어가기
# 첫번쨰 수로 양의 정수가 주어진다
# 두 번째 수는 양의 정수 중에서 하나를 선택한다.
# 세번쨰 수부터는 앞에 2개의 숫자의 차가 온다.
# 입력으로 첫 번째 수가 주어질 때, 이 수에서 시작하여 위 규칙으로 만들어지는 최대 개수의 수들을 구하라.

def minus_Array(start,num) :
    arr = list()
    arr.append(start)
    arr.append(num)
    idx = 2
    while True :
        if arr[idx-2] < arr[idx-1] :
            break
        arr.append(arr[idx-2] - arr[idx-1])
        idx += 1
    return arr

start = int(input())
result = list()
max_arr = list()
max_len = 0
for i in range(start+1) :
    result = minus_Array(start,i)
    if max_len < len(result):
        max_len = len(result)
        max_arr = result
string = ' '.join(map(str,max_arr))
print(max_len)
print(string)