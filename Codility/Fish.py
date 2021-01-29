def solution(A, B):
    # write your code in Python 3.6
    down = []
    result = 0

    for i in range(len(B)):
        if B[i] == 1:
            down.append(A[i])
        else:
            result += 1
            for j in range(len(down) - 1, -1, -1):
                if down[j] > A[i]:
                    result -= 1
                    break
                else:
                    down.pop(len(down) - 1)

    return result + len(down)


A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]

print(solution(A, B))
