# Easy, 44ms

class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        stat = {}; res = ""
        for c in T: stat[c] = stat.get(c, 0) + 1
        for c in S: res += stat.get(c, 0) * c; stat.pop(c, None)
        for c in stat: res += stat[c] * c
        return res
                