class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        gain = []
        num = len(candies) / 2
        reflect = {v : k for k, v in enumerate(candies)}
        if len(reflect) >= num:
            return num
        else:
            return len(reflect)
