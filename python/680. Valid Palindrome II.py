"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
"""

# 需要找到不一致的元素，删除其中一个，再看是否为回文
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return self.isPalindrome(s[:i]+s[i+1:]) or self.isPalindrome(s[:j]+s[j+1:])
            i += 1; j -= 1
        return True
    
    def isPalindrome(self, s):
        return s[::-1] == s