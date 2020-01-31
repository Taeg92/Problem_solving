# Problem [4835] : 구간합
# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 프로그램.
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램.

test_cnt = int(input())

for test in range(1,test_cnt+1):
    max_sum = -100000000000
    min_sum = 100000000000
    arr_size, serch_size = map(int,input().split())
    arr = list(map(int,input().split()))
    for i in range(arr_size-serch_size+1):
        arr_sum = 0
        for j in range(serch_size):
            arr_sum += arr[i+j]
        if arr_sum > max_sum:
            max_sum = arr_sum
        if arr_sum < min_sum:
            min_sum = arr_sum
    print('#{} {}'.format(test,max_sum-min_sum))