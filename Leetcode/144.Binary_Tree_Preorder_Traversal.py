# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.traversal = []

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        self.traversal.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.traversal

# root = [1,null,2,3]
# Output: [1, 2, 3]
