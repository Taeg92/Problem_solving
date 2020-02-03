# Problem [15649] : N과 M(1)

def permutation(arr, r):

    result = list()
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):

        if len(chosen) == r:
            result.append(chosen[:])
	

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)
    return result

n_val, m_val = map(int, input().split())
result = permutation(range(1,n_val+1), m_val)
for i in result:
    print(' '.join(map(str,i)))