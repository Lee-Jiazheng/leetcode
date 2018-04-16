# Easy
class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ver_skyline = list(map(lambda *x: max(*x), *grid))
        hor_skyline = [max(hor) for hor in grid]
        print(ver_skyline, hor_skyline)
        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                sum += min(ver_skyline[j], hor_skyline[i]) - grid[i][j]
        return sum
        
        