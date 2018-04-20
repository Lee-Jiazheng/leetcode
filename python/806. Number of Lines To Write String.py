class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        width = {chr(i+ord('a')): w for i, w in enumerate(widths)}
        lines = 0; char = 0
        for i, s in enumerate(S):
            if char + width[s] > 100: char = 0; lines += 1
            char += width[s]
        return lines+1, char