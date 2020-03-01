# Problem [15657] : N과 M(8)

def repeat_combi(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else :
            for next in repeat_combi(arr[i:],r-1):
                yield [arr[i]] + next

N, M = map(int, input().split())
d = sorted(list(map(int,input().split())))
result = repeat_combi(d, M)
for i in result:
    print(' '.join(map(str,i)))