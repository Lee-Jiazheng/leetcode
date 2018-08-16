"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j == 0: pass
                elif i == 0: dp[j] = dp[j-1]
                else: dp[j] = min(dp[j-1], dp[j])
                dp[j] += grid[i][j]
        return dp[len(grid[0])-1]