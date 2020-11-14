import heapq


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = {}

        for start, end, time in times:
            if start not in graph:
                graph[start] = [(end, time)]
            else:
                graph[start].append((end, time))

        arrive_signal_dict = {}

        queue = [(0, K)]

        while queue:
            time, node = heapq.heappop(queue)
            if node not in arrive_signal_dict:
                arrive_signal_dict[node] = time

                if node in graph:
                    for nxt, delay in graph[node]:
                        arrive_signal_time = time + delay
                        heapq.heappush(queue, (arrive_signal_time, nxt))

        if len(arrive_signal_dict.keys()) == N:
            return max(arrive_signal_dict.values())
        return -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N = 4
K = 2
# Output: 2

sol = Solution()
print(sol.networkDelayTime(times, N, K))
