from collections import defaultdict, deque


def solution(n, vertex):

    def init_graph(vertex):
        result = defaultdict(list)

        for u, v in vertex:
            result[u].append(v)
            result[v].append(u)

        return result

    graph = init_graph(vertex)
    visited = [0] * (n + 1)

    def bfs(s, visited):
        depth = 0
        queue = deque([(s, depth)])
        visited[1] = 1

        while queue:

            cur, depth = queue.popleft()
            for nxt in graph[cur]:
                if not visited[nxt]:
                    queue.append([nxt, depth + 1])
                    visited[nxt] = depth + 1

        return

    def get_farthest_node(visited, max_dist):
        cnt = 0
        for dist in visited:
            if dist == max_dist:
                cnt += 1
        return cnt

    bfs(1, visited)

    max_dist = max(visited)

    return get_farthest_node(visited, max_dist)


n = 6
vertex = [
    [3, 6], [4, 3],
    [3, 2], [1, 3],
    [1, 2], [2, 4],
    [5, 2]
]

print(solution(n, vertex))
