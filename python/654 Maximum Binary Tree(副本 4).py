# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None    

class Solution(object):
    def findMaxIndex(self, nums):
        max = -1
        maxIndex = 0
        for i in range(len(nums)):
            if nums[i] > max:
                maxIndex = i
                max = nums[i]
        return maxIndex

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        index = self.findMaxIndex(nums)
        node = TreeNode(nums[index])
        node.left  = self.constructMaximumBinaryTree(nums[:index])
        node.right = self.constructMaximumBinaryTree(nums[index+1:])
        return node
