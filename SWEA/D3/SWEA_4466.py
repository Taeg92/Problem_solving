# Problem [4466] : 최대 성적표 만들기

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    data = sorted(list(map(int,input().split())))
    s = 0
    for _ in range(K):
        s += data.pop()
    print('#{} {}'.format(tc,s))
