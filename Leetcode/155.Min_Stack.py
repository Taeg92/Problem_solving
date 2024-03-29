class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.__stack:
            self.__stack.append(
                (x, min(x, self.__stack[-1][1])))
        else:
            self.__stack.append((x, x))

    def pop(self):
        """
        :rtype: None
        """
        if self.__stack:
            self.__stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.__stack:
            return self.__stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.__stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
