# Problem [15650] : N과 M(2)

def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combination(arr[i+1:],r-1):
                yield [arr[i]] + next

    

n_val, m_val = map(int, input().split())
result = combination(range(1,n_val+1), m_val)
for i in result:
    print(' '.join(map(str,i)))