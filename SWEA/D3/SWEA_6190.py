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
 
 
def recursion(arr,n):
    global m
    if n == N and m == 0:
        m = -1
    elif n == N and m != 0:
        return
    else:
        for i in range(n+1,N):
            if is_Increase(arr[n]*arr[i]) and arr[n]*arr[i] > m :
                m = arr[n]*arr[i]
                break
        recursion(arr,n+1) 
 
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = sorted(list(map(int, input().split())),reverse=True)
    m = 0
    recursion(data,0)
    print('#{} {}'.format(tc,m))