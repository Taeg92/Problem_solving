# Problem [2559] : 수열
# 입력 첫째 줄에 정수 N과 K가 주어진다. N : 날짜수 K :연속 수
# 입력 둘째 줄에는 측정한 온도들이 N개 주어진다.

def Prefix_Sum(arr,K):
    section_sum = sum(arr[0:K])
    m = section_sum
    i = 0
    if K == 1:
        return max(arr)
    else:
        while 1:
            if i + K > N-1:
                break
            section_sum -= arr[i]
            section_sum += arr[i+K]
            i += 1
            if section_sum > m:
                m = section_sum
        return m
            


N, K = map(int,input().split())
data = list(map(int,input().split()))

m = Prefix_Sum(data,K)
print(m)

