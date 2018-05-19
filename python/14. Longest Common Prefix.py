"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        for i, letter_group in enumerate(zip(*strs)):
            # letter_group is ('f', 'f', 'f') \ ('l', 'l', 'l') \ ('o', 'o', 'i')
            if len(set(letter_group)) > 1:
                return(strs[0][:i])
        
        return min(strs)


        # import os 
        # return os.path.commonprefix(strs)