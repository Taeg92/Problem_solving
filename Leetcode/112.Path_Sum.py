# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def DFS(root, targetSum, curr):
            if root:
                curr += root.val
                if curr == targetSum and root.left == None and root.right == None:
                    return True
                return DFS(root.left, targetSum, curr) or DFS(root.right, targetSum, curr)
        return DFS(root, targetSum, 0)

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
