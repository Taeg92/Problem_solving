# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.traversal = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        self.inorderTraversal(root.left)
        self.traversal.append(root.val)
        self.inorderTraversal(root.right)

        return self.traversal


# root = [1, null, 2, 3]
# Output: [1, 3, 2]
