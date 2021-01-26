def solution(A):
    # write your code in Python 3.6
    if len(A) < 2:
        return 0

    max_profit = 0

    min_price = A[0]

    for i in range(1, len(A)):
        profit = A[i] - min_price
        if profit > 0:
            max_profit = max(max_profit, A[i] - min_price)
        else:
            min_price = A[i]

    return max_profit


A = [23171, 21011, 21123, 21366, 21013, 21367]

print(solution(A))
