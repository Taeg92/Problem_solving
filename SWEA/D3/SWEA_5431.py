# Problem [5431] : 민석이의 과제 체크하기

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    data = list(map(int,input().split()))
    result = list()
    for i in range(1,N+1):
        if i not in data:
            result.append(i)
    print('#{} {}'.format(tc,' '.join(map(str,result))))