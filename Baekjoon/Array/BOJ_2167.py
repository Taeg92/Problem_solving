# Problem : 2차원 배열의 합

N, M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * (M + 1) for _ in range(N + 1)]      

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = data[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

K = int(input())
for i in range(K):
    s = 0
    sc, sr, ec, er = map(int,input().split())
    s += dp[ec][er] - dp[sc-1][er] - dp[ec][sr-1] + dp[sc-1][sr-1]
    print(s)
