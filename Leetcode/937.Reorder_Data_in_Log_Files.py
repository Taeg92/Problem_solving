class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters, digits = self.separateLogs(logs)

        letters = self.reorderLetters(letters)

        return letters + digits
    
    def separateLogs(self, logs):
        letters, digits = [], []
        for log in logs:
            val = log.split()[1]
            if val.isdigit():
                digits.append(log)
            else:
                letters.append(log)
        return letters, digits

    def reorderLetters(self, letters):
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

sol = Solution()
print(sol.reorderLogFiles(logs))