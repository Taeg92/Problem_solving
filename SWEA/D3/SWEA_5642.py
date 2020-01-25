# Problem [5642] : [Professional] 합
# N개의 정수가 입력으로 주어 질 때, 연속으로 몇개의 정수를 골라 최대가 몇인지 구하는 프로그램.

def dynamic_programming(arr):
    cache = [None] * len(arr)
    # 1.
    cache[0] = arr[0]

    # 2.
    for i in range(1, len(arr)):
        cache[i] = max(0, cache[i-1]) + arr[i]

    return max(cache)

test_cnt = int(input())
for test in range(1, test_cnt+1):
    n_val = int(input())
    numbers = list(map(int,input().split()))
    result = dynamic_programming(numbers) 
    print('#{} {}'.format(test,result))