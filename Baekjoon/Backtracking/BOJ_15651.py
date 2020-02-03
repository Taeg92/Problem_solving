# Problem [15651] : N과 M(3)

def product(arr,r):
    for i in range(len(arr)):  
        if r == 1:  
            yield [arr[i]]
        else:
            for next in product(arr,r-1): 
                yield [arr[i]] + next


N, M = map(int,input().split())
result = list(product(range(1,N+1),M))
for n in result:
    print(' '.join(map(str,n)))
