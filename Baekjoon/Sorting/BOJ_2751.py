# Problem [2751] : 수 정렬하기 2

n_val = int(input())
result = list(sorted([int(input()) for _ in range(n_val)]))
for n in result:
    print(n)