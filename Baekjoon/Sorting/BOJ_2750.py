# Problem [2750] : 수 정렬하기
# N개의 수가 주어졌을 때 오름차순으로 정렬하는 프로그램.

def bubble_sort(arr):
    length = len(arr) - 1
    for i in range(length):
        for j in range(length-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

n_val = int(input())
num = [int(input()) for _ in range(n_val)]
result = bubble_sort(num)
for n in result:
    print(n)