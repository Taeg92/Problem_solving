# Problem [2001] : 파리퇴치
# N X N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
# M X M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
# 죽은 파리의 최대 개수를 구하라.


def numFly(arr,N,M):  
    result = list()
    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0
            for k in range (M):
                s += sum(arr[i+k][j:j+M])
            result.append(s)
    return max(result)

T = int(input())   

for tc in range(1, T+1):
    N, M = map(int,input().split())
    d = [list(map(int,input().split())) for _ in range(N)]
    result = numFly(d,N,M)
    print('#{} {}'.format(tc,result))