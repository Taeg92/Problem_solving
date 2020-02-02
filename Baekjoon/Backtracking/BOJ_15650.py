# Problem [14539] : N과 M(2)

def combination(arr, r):

    result = list()
    arr = sorted(arr)

    def generate(chosen):
        if len(chosen) == r:
            result.append(chosen[:])

        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for i in range(start, len(arr)):
            chosen.append(arr[i])
            generate(chosen)
            chosen.pop()
    generate([])

    return result

n_val, m_val = map(int, input().split())
result = combination(range(1,n_val+1), m_val)
for i in result:
    print(' '.join(map(str,i)))