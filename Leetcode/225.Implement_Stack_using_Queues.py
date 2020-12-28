from collections import deque


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.stack) == 0


myStack = MyStack()
myStack.push(1)
print(myStack.stack)
myStack.push(2)
print(myStack.stack)
myStack.top()
print(myStack.stack)
# return 2
myStack.pop()
print(myStack.stack)
# return 2
myStack.empty()
print(myStack.stack)
# return False
