from collections import deque

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = deque([(root.left, root.right)])
        while stack:
            l, r = stack.pop()
            if l is None and r is None:
                continue
            if l is None or r is None:
                return False
            if l.val != r.val:
                return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True


# root = [1, 2, 2, 3, 4, 4, 3]
# Output: true
