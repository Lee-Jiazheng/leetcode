# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [(root, 1)]
        maxdepth = 0
        maxval = None
        while queue:
            cur, depth = queue[0]
            queue.pop(0)
            if cur.left != None:
                queue.append((cur.left, depth+1))
            if cur.right != None:
                queue.append((cur.right, depth+1))
            if depth > maxdepth:
                maxval = cur.val
                maxdepth = depth
        return maxval
