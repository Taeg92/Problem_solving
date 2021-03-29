from collections import deque


def solution(n, computers):
    answer = 0

    check = [0] * n

    def bfs(start):

        queue = deque([start])

        while queue:

            node = queue.popleft()

            for i in range(len(computers)):
                if not check[i]:
                    if computers[i][node]:
                        queue.append(i)
                        check[i] = 1

        return

    for i in range(len(check)):
        if not check[i]:
            answer += 1
            bfs(i)

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]


print(solution(n, computers))
