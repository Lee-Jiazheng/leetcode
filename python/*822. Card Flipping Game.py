# https://leetcode.com/contest/weekly-contest-81/problems/card-flipping-game/

# 正反面相同的卡拍就一定不是good number， 注意：可以翻(flip)任意数量的牌
class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        probs = set(fronts).union(set(backs)) - set([fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i]])
        return sorted(probs)[0] if probs else 0 