class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        num_list = list(str(x))
        size = len(num_list)
        for i in range(len(num_list) // 2):
            if num_list[i] != num_list[size - 1 - i]:
                return False
        return True


x = 121

sol = Solution()

print(sol.isPalindrome(x))
