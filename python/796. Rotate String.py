# Easy
"""
遍历位置，如果A的右边字符串加左边字符串就是B则可以shift。
注意两个都是空字符串的情况
"""

class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B: return True
        for i in range(len(A)):
            if A[i:] + A[:i] == B: return True
        return False