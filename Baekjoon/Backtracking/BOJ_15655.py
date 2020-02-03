# Problem [15655] : N과 M(6)

def combination(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else :
            for next in combination(arr[i+1:],r-1):
                yield [arr[i]] + next

N, M = map(int, input().split())
d = sorted(list(map(int,input().split())))
result = combination(d, M)
for i in result:
    print(' '.join(map(str,i)))