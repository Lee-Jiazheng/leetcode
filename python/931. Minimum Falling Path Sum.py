"""
Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.

 

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation: 
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.

 

Note:

1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100

"""

# 下一行的选择不能在上一行选择列的偏差超过1
class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        rows = cols = len(A)
        dp = [[0]*cols for _ in range(rows)]
        # dp can just be A
        dp[0][:] = A[0]
        
        for r in range(1, rows):
            for c in range(0, cols):
                # It means [(c and c-1):c+2]
                dp[r][c] = A[r][c] + min(dp[r-1][c and c-1:c+2])    
        return min(dp[-1])