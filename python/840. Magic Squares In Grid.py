"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an N x N grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

 

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length = grid[0].length <= 10
0 <= grid[i][j] <= 15
"""

class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def get(i, j):
            return grid[i][j]
        if len(grid) < 3: return 0
        res = 0
        for i in range(len(grid)-2):
            for j in range(len(grid)-2):
                arr = [get(_row, _col) for _row, _col in itertools.product((i, i+1, i+2), (j, j+1, j+2))]
                
                if sorted(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    if arr[0]+arr[3]+arr[6] == arr[1]+arr[4]+arr[7] == arr[2]+arr[5]+arr[8] == arr[0]+arr[4]+arr[8] == arr[2]+arr[4]+arr[6]:
                        res += 1
        return res