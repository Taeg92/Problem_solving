def solution(A):
    # write your code in Python 3.6
    if max(A) != len(A) or len(set(A)) != len(A):
        return 0
    return 1


A = [4, 1, 3]
B = [4, 1, 3, 2]

print(solution(A), solution(B))
