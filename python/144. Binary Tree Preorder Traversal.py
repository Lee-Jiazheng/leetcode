# 非递归方式
# 把右节点放入栈中，左节点的值为结果。 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            while node:
                res.append(node.val)
                stack.append(node.right)
                node = node.left
        return res