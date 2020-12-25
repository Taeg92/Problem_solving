import heapq


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))

        answer = []
        for _ in range(K):
            dist, x, y = heapq.heappop(heap)
            answer.append((x, y))
        return answer


sol = Solution()

points = [[3, 3], [5, -1], [-2, 4]]
K = 2

print(sol.kClosest(points, K))
