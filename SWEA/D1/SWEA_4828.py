# Problem [4828] : min, max 구하기
# min,max 함수를 사용하지 않고 구하기.

def find_max(arr):
    max_val = -100000000000000000
    for i in range(len(arr)):
        if arr[i] > max_val :
            max_val = arr[i]
    return max_val

def find_min(arr):
    min_val = 100000000000000000
    for i in range(len(arr)):
        if arr[i] < min_val :
            min_val = arr[i]
    return min_val

test_cnt = int(input())

for test in range(1,test_cnt+1):
    arr_max = 0
    arr_min = 1000000000000000
    size = int(input())
    arr = list(map(int,input().split()))
    arr_max = find_max(arr)
    arr_min = find_min(arr)
    result = arr_max - arr_min
    print('#{} {}'.format(test,result))