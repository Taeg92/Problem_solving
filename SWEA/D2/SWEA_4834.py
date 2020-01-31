# Problem [4834] : 숫자카드
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램

def find_max(arr):
    max_val = -100000000000000000
    for i in range(len(arr)):
        if arr[i] >= max_val :
            max_val = arr[i]
    return max_val

test_cnt = int(input())
for test in range(1,test_cnt+1):
    size = int(input())
    numbers = list(map(int,list(input())))
    num_dict = dict()
    max_key = 0
    max_val = 0
    for i in range(size):
        if numbers[i] not in num_dict:
            num_dict[numbers[i]] = 1
        else:
            num_dict[numbers[i]] += 1
    max_val = find_max(list(num_dict.values()))

    for key,value in num_dict.items():
        if value == max_val:
            key_list = [k for k,v in num_dict.items() if v == max_val]
            max_key = max(key_list)
    print('#{} {} {}'.format(test,max_key,max_val))
