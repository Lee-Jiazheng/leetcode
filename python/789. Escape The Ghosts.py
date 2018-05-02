# 计算Ghost和人哪个先到target。
class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        for g in ghosts:
            if abs(target[0]-g[0])+abs(target[1]-g[1]) <= abs(target[0])+abs(target[1]): return False
        return True