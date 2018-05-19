"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, end, mx = 0, 0, -1
        while end <= len(s):
            if end == len(s):
                if end - start > mx:
                    mx = end - start
            elif s[end] in s[start:end]:
                mx = max(mx, end-start)
                start = s[start:end].index(s[end]) + start + 1
            end += 1
        return mx if mx != -1 else 0