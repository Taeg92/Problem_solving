# Problem [15652] : N과 M(4)

def repeat_conb(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in repeat_conb(arr[i:],r-1):
                yield [arr[i]] + next


N, M = map(int,input().split())
result = list(repeat_conb(range(1,N+1),M))
for n in result:
    print(' '.join(map(str,n)))