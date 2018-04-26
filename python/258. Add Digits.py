"""
Digital root: https://en.wikipedia.org/wiki/Digital_root
For base b (decimal case b = 10), the digit root of an integer is:

dr(n) = 0 if n == 0
dr(n) = (b-1) if n != 0 and n % (b-1) == 0
dr(n) = n mod (b-1) if n % (b-1) != 0
or

dr(n) = 1 + (n - 1) % 9
Note here, when n = 0, since (n - 1) % 9 = -1, the return value is zero (correct).

注意： Python, -1 % 9 = 8
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0: return 0
        return 1 + (num - 1) % 9