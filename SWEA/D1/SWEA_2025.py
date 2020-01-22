# Problem [2025] 1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.
# 단, 주어질 숫자는 10000을 넘지 않는다.

def calc_Sum(n):
    sum = n*(n+1)/2
    return int(sum)

num = int(input())
result = calc_Sum(num)
print(result)