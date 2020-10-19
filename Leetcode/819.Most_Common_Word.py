import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        word_list = self.getWordList(paragraph)
        word_dict = self.getWordDict(word_list, banned)

        most_common_word = max(word_dict.keys(), key=lambda x: word_dict[x])
        
        return most_common_word

    def getWordList(self, paragraph):
        regex = '[a-zA-Z]+'
        return re.findall(regex, paragraph)
    
    def getWordDict(self, words, banned):
        word_dict = {}
        for word in words:
            word = word.lower()
            if word not in banned:
                if word not in word_dict:
                    word_dict[word] = 1
                else:
                    word_dict[word] += 1
        return word_dict
    

# input
paragraph = "Bob. hIt, baLl"
banned = ["bob", "hit"]
# output "ball"


sol = Solution()
print(sol.mostCommonWord(paragraph, banned))
