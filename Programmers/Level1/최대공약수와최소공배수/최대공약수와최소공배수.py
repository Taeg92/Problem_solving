def solution(n, m):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            if m % i == 0:
                gcd = i
    if gcd == 1:
        lcm = n*m
    else:
        lcm = gcd * (n // gcd) * (m // gcd)
    answer.extend([gcd, lcm])
    return answer

n = 3
m = 12
print(solution(n, m))