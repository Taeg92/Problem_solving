class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return format(int(a, 2) + int(b, 2), 'b')


a = "11"
b = "1"

sol = Solution()

print(sol.addBinary(a, b))
