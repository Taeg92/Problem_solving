class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        total_area = 0

        for i in range(len(height)):
            
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break
                distance = i - stack[-1] - 1
                area = min(height[i], height[stack[-1]]) - height[top]

                total_area += distance * area

            stack.append(i)
        return total_area

height = [4,2,0,3,2,5]
# Output: 9

sol = Solution()
print(sol.trap(height))
