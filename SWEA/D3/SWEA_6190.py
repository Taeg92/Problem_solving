# Problem [6190] : 정곤이의 단조 증가하는 수
# 입력 첫째 줄 : 테스트 케이스
# 입력 받는 숫자의 개수 N
# N개의 수를 입력

# def is_Increase(arr,n):
#     global prev
#     if n == N:
#         return
#     else:
#         for i in range(N):
#             if arr[n]*arr[i] > prev:
#                 prev = arr[n]*arr[i]
#                 is_Increase(arr,n+1)



# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     numbers = [list(map(int,input().split())) for _ in range(N)]
#     prev = 0
#     is_Increase(numbers,0)
#     print(prev)
def chk_danjo(num):
    while num > 0:
        num, r = divmod(num, 10)
        if not num % 10 <= r:
            return False
    return True

def dfs(level, selected, product):
    global max_result
    if selected == 2:
        if product < max_result: return
        if chk_danjo(product):
            max_result = product
            return
    if level == n: 
        return
    dfs(level+1, selected + 1, product * ns[level])
    dfs(level+1, selected, product)
    
T = int(input())
for t in range(1, T+1):
    n = int(input())
    ns = list(map(int, input().split()))
    max_result = 0
    dfs(0, 0, 1)
    if max_result == 0:
        print("#{} {}".format(t, -1))
    else:
        print("#{} {}".format(t, max_result))