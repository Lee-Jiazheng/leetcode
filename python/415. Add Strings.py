"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        add = 0
        res = ""
        len_d = len(num1) - len(num2)
        if len_d < 0: num1 = "0"*-len_d + num1
        else: num2 = "0"*len_d + num2
        for n1, n2 in zip(num1[::-1], num2[::-1]):
            s = ord(n1)-48 + ord(n2)-48 + add
            if s >= 10:
                s -= 10; add = 1
            else: add = 0
            res += (chr(s+48))
        if add == 1: res += "1"
        return res[::-1]