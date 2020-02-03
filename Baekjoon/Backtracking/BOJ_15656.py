# Problem [15656] : N과 M(7)

def product(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else :
            for next in product(arr,r-1):
                yield [arr[i]] + next

N, M = map(int, input().split())
d = sorted(list(map(int,input().split())))
result = product(d, M)
for i in result:
    print(' '.join(map(str,i)))