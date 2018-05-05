class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        point = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        begin = 0; points = [0]
        for _s in s:
            if point[_s] > points[-1]:
                points.extend([-2*points[-1], point[_s]])
            else:
                points.append(point[_s])
        return sum(points)