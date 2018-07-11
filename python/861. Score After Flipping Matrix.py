"""
We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.

 

Example 1:

Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

 

Note:

    1 <= A.length <= 20
    1 <= A[0].length <= 20
    A[i][j] is 0 or 1.
"""

class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def flip_col(_A, i):
            for j, _a in enumerate(A[i]):
                A[i, j] = 1 if _a == 0 else 0
        
        def flip_row(_A, j):
            for i in range(len(A)):
                A[i, j] = 1 if A[i, j] == 0 else 0
        import numpy as np
        A = np.array(A)
        for i, a in enumerate(A):
            if a[0] != 1:
                flip_col(A, i)
        
        for i in range(1, len(A[0])):
            if len(list(filter(lambda x: x == 1, A[: ,i]))) < len(A)/2:
                flip_row(A, i)
        s = 0
        for i in range(len(A[0])):
            s += 2**(len(A[0])-i-1)*len(list(filter(lambda x: x == 1, A[: ,i])))
        return s