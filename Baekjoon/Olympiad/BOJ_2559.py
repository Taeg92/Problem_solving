# Problem [2559] : 수열
# 입력 첫째 줄에 정수 N과 K가 주어진다. N : 날짜수 K :연속 수
# 입력 둘째 줄에는 측정한 온도들이 N개 주어진다.


N, K = map(int,input().split())
data = list(map(int,input().split()))
m = 0
for i in range(len(data)-K):
    if m < sum(data[i:i+K]):
        m = sum(data[i:i+K])
print(m)