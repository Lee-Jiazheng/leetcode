class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = []
        res = 0
        while num != 0:
            binary.append(num % 2)
            num /= 2
        multiple = 1
        for b in binary:
            if b == 0:
                res += multiple
            multiple *= 2
        return res
                
