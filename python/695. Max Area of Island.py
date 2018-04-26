class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return max([max([self.dfs(grid, x, y) for y, _g in enumerate(g)]) for x, g in enumerate(grid)])
    
    def dfs(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0: return 0
        grid[x][y] = 0
        return 1 + self.dfs(grid, x-1, y) + self.dfs(grid, x+1, y) + self.dfs(grid, x, y+1) + self.dfs(grid, x, y-1)