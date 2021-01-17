def solution(A, B, K):
    # write your code in Python 3.6
    answer = B // K - A // K
    if A % K:
        return answer
    return answer + 1


A = 6
B = 11
K = 2

print(solution(A, B, K))
