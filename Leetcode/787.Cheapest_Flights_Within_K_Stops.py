import heapq


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = {}
        for start, end, cost in flights:
            if start not in graph:
                graph[start] = [(end, cost)]
            else:
                graph[start].append((end, cost))

        queue = [(0, src, K)]

        while queue:
            price, cur, k = heapq.heappop(queue)
            if cur == dst:
                return price
            if k > -1:
                if cur in graph:
                    for nxt in graph[cur]:
                        heapq.heappush(queue, (price + nxt[1], nxt[0], k-1))
        return -1


n = 3
flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
k = 0

sol = Solution()
print(sol.findCheapestPrice(n, flights, src, dst, k))
