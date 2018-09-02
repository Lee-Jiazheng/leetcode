"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""

class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0: return
        m, n = len(board), len(board[0])
        
        outer = "T"
        def dfs(x, y):
            if x<0 or y<0 or x>=m or y>=n or board[x][y]!="O": return 0
            board[x][y] = outer
            dfs(x-1, y) + dfs(x, y-1) + dfs(x+1, y) + dfs(x, y+1); return 0
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for i in range(n):
            dfs(0, i)
            dfs(m-1, i)
        
        for i in range(m):
            for j in range(n):
                board[i][j] = ("O" if board[i][j] == outer else "X")
        
        