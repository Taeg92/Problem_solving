# Problem [1859] : 백만장자 프로젝트
# 미래를 보고 매매가를 알 수 있을 때 사재기를 통해 최대한의 이득을 구하기.
# 첫번째 줄에 테스트 케이스 T
# 각 스트 케이스 별로 첫 줄에는 자연수 N이 주어지고 둘 째 줄에는 각 날의 매매가를 나타내는 N개의 자연수들이 공백으로 구분되어 입력된다.


test_cnt = int(input())
for test in range(1,test_cnt+1) :
    n_val = int(input())
    price = list(map(int,input().split()))
    profit = 0
    max_price = 0
    for i in range(n_val) :
        if max_price < price[-(i+1)] :
            max_price = price[-(i+1)]
        profit += (max_price - price[-(i+1)])
    print('#{} {}'.format(test,profit))

















# for T in range(int(input())):
#     N = int(input())
#     price = list(map(int, input().split()))
#     profit, max_ = 0, 0
#     for i in range(N):
#         if max_ < price[-i-1]:
#             max_ = price[-i-1]
#         profit += (max_ - price[-i-1])
#     print(f'#{T+1} {profit}')