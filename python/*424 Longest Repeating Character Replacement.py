class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0
        str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        dict = {}
        for i in str:
            dict[i] = 0
        most_count = 1     # current most character count
        left = 0
        result = 1
        dict[s[0]] = 1
        for i in range(1, len(s)):
            dict[s[i]] += 1
            most_count = max(most_count, dict[s[i]])
            if most_count + k < i - left + 1:
                dict[s[left]] -= 1
                left += 1
            result = max( result, i - left + 1)
        return result 
