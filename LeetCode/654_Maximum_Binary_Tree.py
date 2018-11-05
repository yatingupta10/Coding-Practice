# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 1:
            return TreeNode(nums[0])
        elif not nums:
        	return None

        max_temp = [float("-inf"), 0]
        for i, element in enumerate(nums):
            if element > max_temp[0]:
                max_temp[0] = element
                max_temp[1] = i

        root = TreeNode(max_temp[0])
        root.left = self.constructMaximumBinaryTree(nums[:max_temp[1]])
        root.right = self.constructMaximumBinaryTree(nums[max_temp[1] + 1:])

        return root