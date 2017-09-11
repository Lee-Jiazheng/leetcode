class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        row = len(board)
        col = len(board[0])
        count = 0
        
        # 船头个数，船头的左边和上边一定是空的，也就是为'.'或者左上两边，因为是水平排列按顺序数
        for i in range(row):
            for j in range(col):
                if (i==0 or board[i-1][j]=='.') and (j==0 or board[i][j-1]=='.') and board[i][j]=='X':
                    count += 1
        return count
