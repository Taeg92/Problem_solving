# Problem [2731] : 분해합
# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다.
# 예를 들어 245의 분해합은 245+2+4+5로 256이 정답이다.

n_val = int(input())
n = 0
while n < n_val:
    if n_val == 1:
        n = 0
        break
    total_sum = n
    start = n
    for _ in range(len(str(start))):
        total_sum += start % 10
        start //= 10
    if total_sum == n_val :
        break
    n += 1
    if n == n_val :
        n = 0
        break
print(n)