class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res_ = []
        for num in range(left, right+1):
            for n in str(num):
                if n == '0' or num % int(n) != 0:
                    res_.append(num); break
        return [num for num in range(left, right+1) if num not in res_]


class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [n for n in range(left, right+1) if not any([dig == '0' or n % int(dig) != 0 for dig in str(n)])]