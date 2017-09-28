class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1, a2 = a.split('+')
        b1, b2 = b.split('+')
        a2 = a2[:-1]
        b2 = b2[:-1]
        return str(int(a1) * int(b1) - int(a2) * int (b2)) + '+' + str((int(a1) * int(b2) + int(b1) * int(a2))) + 'i'
        
