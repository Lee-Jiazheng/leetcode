"""Hard

Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"
Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
"""

class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        K = len(n)
        # 考虑进位情况，如果1000的话，下限为999（为回文数），上限为9999。
        candidates = [10**k+d for k in (K-1, K) for d in (-1, 1)]  
        prefix = int(n[:(K+1)//2])  # 获取前缀，如1234获取12,12345获取123
        # 添加候选，1221\1111\1331的情况。
        candidates += [int(p + (p[:-1] if K%2 else p)[::-1]) for p in map(str, [prefix-1, prefix, prefix+1])]
        # 去除n
        candidates = list(filter(lambda x: x != int(n), candidates)) if int(n) in candidates else candidates
        # 找到最相近的，如果相同则找到更小的那个。
        return str(sorted([(abs(candidate-int(n)), candidate) for candidate in candidates])[0][1])
                