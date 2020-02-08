# Problem [8706] : 당근 수확 2

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    d = list(map(int,input().split()))
    dist = 0
    r = M

    for i in range(N):
        while d[i] >= r:
            d[i] -= r
            dist += (i+1)*2
            r = M
        r -= d[i]
        dist += 1
    dist += N
    
    print('#{} {}'.format(tc,dist))