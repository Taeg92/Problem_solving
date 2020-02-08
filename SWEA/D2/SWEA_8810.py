# Problem [8810] : 당근밭 옆 고구마밭

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = list(map(int,input().split()))
    result = list()
    temp = [d[0]]
    max_len = 0
    max_sum = 0
    cnt = 0
    for i in range(N-1):
        if d[i] < d[i+1]:
            temp.append(d[i+1])
        else:
            result.append(temp)
            temp = [d[i+1]]
        if i == N-2:
            result.append(temp)
    for stem in result:
        if len(stem) > 1:
            if max_len < len(stem):
                max_len = len(stem)
                max_sum = sum(stem)
            if len(stem) == max_len:
                if sum(stem) > max_sum:
                    max_sum = sum(stem)
            cnt += 1
    print('#{} {} {}'.format(tc,cnt,max_sum))
    