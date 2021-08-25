# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None

        mid = nums[len(nums) // 2]

        root = TreeNode(mid)
        root.left = self.sortedArrayToBST(nums[:len(nums) // 2])
        root.right = self.sortedArrayToBST(nums[len(nums) // 2 + 1:])

        return root


nums = [1, 3]
# Output : [3, 1]
