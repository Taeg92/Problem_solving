from collections import defaultdict


def solution(tickets):
    tickets.sort()

    visited = [0] * len(tickets)
    result = []
    answer = ["ICN"]

    def dfs(start, visited, result):

        for i in range(len(tickets)):
            if not visited[i] and start == tickets[i][0]:
                visited[i] = 1
                result.append(i)
                dfs(tickets[i][1], visited, result)
                if sum(visited) == len(tickets):
                    return
                else:
                    result.pop()
                    visited[i] = 0

    dfs("ICN", visited, result)

    for i in result:
        answer.append(tickets[i][1])

    return answer


tickets = [
    ["ICN", "SFO"], ["ICN", "ATL"],
    ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]
]

print(solution(tickets))
