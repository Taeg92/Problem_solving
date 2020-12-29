class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = list()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.queue:
            return self.queue.pop(0)
        return 0

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.queue:
            return self.queue[0]
        return 0

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.queue) == 0


myQueue = MyQueue()
myQueue.push(1)
# queue is: [1]
myQueue.push(2)
# queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek()
# return 1
myQueue.pop()
# return 1, queue is [2]
myQueue.empty()
# return false
