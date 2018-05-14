# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        self.lst = [[] for _ in range(10)]
        self.construct(root, 0)
        print(self.lst)
        for depth, l in enumerate(self.lst): 
            if not any(l): break
        
        res = []
        for i in range(depth):
            print(i)
            void = [""]*(pow(2,depth-1-i)-1)
            print(void)
            temp = []
            for c, num in enumerate(self.lst[i]):
                temp += void + [num] + void + ([""] if c != len(self.lst[i])-1 else [])
            res.append(temp)
        return res
    
    def construct(self, node, depth):
        if depth == 10: return
        node = node if node else TreeNode("")
        self.lst[depth].append(str(node.val))
        self.construct(node.left, depth+1)
        self.construct(node.right, depth+1)