# Problem [2108] : 통계학
# 첫째 줄 : 산술 평균 (소수점 이하 첫째 자리에서 반올림)
# 둘째 줄 : 중앙값
# 셋째 줄 : 최빈값 (여러 개 있을 때 두 번째로 작은 값)
# 넷째 줄 : 범위(최대 - 최소)

import sys

def find_mode(arr):
    count = dict()

    for num in arr:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    
    mode = list(sorted([key for key,val in count.items() if val == max(count.values())]))
    
    if len(mode) > 1 :
        return mode[1]
    return mode[0]

n_val = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n_val)]
mean = round((sum(numbers)/n_val))
mid = list(sorted(numbers))[n_val//2]
mode = find_mode(numbers)
n_range = max(numbers) - min(numbers)

print(mean)
print(mid)
print(mode)
print(n_range)