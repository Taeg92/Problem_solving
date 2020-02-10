# Problem [2309] : 일곱 난쟁이

def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combination(arr[i+1:],r-1):
                yield [arr[i]] + next


data = [int(input()) for _ in range(9)]
choice = list(combination(data,7))
result = list()
for c in choice:
    if sum(c) == 100:
        result = c

for n in sorted(result):
    print(n)
