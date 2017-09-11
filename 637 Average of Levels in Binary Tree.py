# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        current = [root]
        next = []
        res = [root.val]
        while True:
            while current:
                ele = current[0]
                current.pop(0)
                if ele.left != None:
                    next.append(ele.left)
                if ele.right != None:
                    next.append(ele.right)
            if len(next) == 0:
                break
            sum = 0.0
            for i in next:
                sum += i.val
            sum /= len(next)
            res.append(sum)
            current = next
            next = []
        return res
