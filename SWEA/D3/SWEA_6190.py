# Problem [6190] : 정곤이의 단조 증가하는 수
# 입력 첫째 줄 : 테스트 케이스
# 입력 받는 숫자의 개수 N
# N개의 수를 입력

def is_Increase(n):
    while n > 0:
        n, r = divmod(n, 10)
        if not n % 10 <= r:
            return False
    return True

def find_max(arr) :
    m = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if is_Increase(data[i]*data[j]):
                if m < data[i]*data[j]:
                    m = data[i]*data[j]
    if m == 0:
        return -1 
    return m


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = sorted(list(map(int, input().split())),reverse=True)
    result = find_max(data)
    print('#{} {}'.format(tc,result))
