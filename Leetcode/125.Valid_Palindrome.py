class Solution(object):
    def isPalindrome(self, s):
        tokens = []
        for char in s:
            if char.isalnum():
                tokens.append(char.lower())
        
        while len(tokens) > 1:
            if tokens.pop() != tokens.pop(0):
                return False
        return True

sol = Solution()

input1 = "A man, a plan, a canal: Panama"
input2 = "race a car"
print("Input: A man, a plan, a canal: Panama\nOutput: " ,sol.isPalindrome(input1))
print("Input: race a car\nOutput: ", sol.isPalindrome(input2))
        