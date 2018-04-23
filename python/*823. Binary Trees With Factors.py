# https://leetcode.com/contest/weekly-contest-81/problems/binary-trees-with-factors/
# Dynamic programming

class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        dp = {}
        # 只有大数可以除开小数
        for i in range(len(A)):
            dp[A[i]] = 1
            for j in range(i):
                if A[i] % A[j] == 0 and A[i] / A[j] in dp:
                    dp[A[i]] += dp[A[j]] * dp[A[i] / A[j]]
        return sum(dp.values()) % (10**9 + 7)