"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

"""

# 指定两个指针，指向反转的两个字符，注意交换后指针需要移动
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i, j = 0, len(s)-1
        while i < j:
            if s[i] not in vowels: i += 1
            elif s[j] not in vowels: j -= 1
            else: s[i], s[j] = s[j], s[i]; i += 1; j -= 1
        return "".join(s)