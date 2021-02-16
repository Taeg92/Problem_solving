class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        start = 0
        end = len(height)-1
        max_area = 0
        while end > start:
            max_area = max(max_area, (end-start) *
                           min(height[start], height[end]))

            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return max_area


height = [4, 3, 2, 1, 4]

sol = Solution()
print(sol.maxArea(height))
