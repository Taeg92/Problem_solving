def solution(X, A):
    # write your code in Python 3.6
    if len(set(A)) != X:
        return -1

    visited = [0] * X
    cnt = 0
    for idx, val in enumerate(A):
        if not visited[val - 1]:
            visited[val - 1] = 1
            cnt += 1
            if cnt == X:
                return idx
    return -1


X = 5
A = [1, 3, 1, 4, 2, 3, 5, 4]

print(solution(X, A))
