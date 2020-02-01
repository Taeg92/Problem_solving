# Problem [10814] : 나이순 정렬

n_val = int(input())
people = [input().split() for _ in range(n_val)]

result = list(sorted(people,key = lambda x : int(x[0])))

for i in range(n_val):
    print('{} {}'.format(result[i][0],result[i][1]))