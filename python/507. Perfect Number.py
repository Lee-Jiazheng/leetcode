class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0 or num == 1: return False    # Expect itself, i.e. 1
        res = [1]
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                res.extend([i, num / i])
        return sum(res) == num