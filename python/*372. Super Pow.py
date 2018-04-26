# 2, [3, 1, 2]
# 2^312 = (2^3)^10 * 2^2 % 1337
class Solution(object):
    def powmod(self, a, k):
        a %= 1337
        return pow(a, k) % 1337
    
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if not b: return 1
        return self.powmod(self.superPow(a, b[:-1]), 10) * self.powmod(a, b[-1]) % 1337