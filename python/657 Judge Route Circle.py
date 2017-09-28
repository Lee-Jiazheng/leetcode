class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        U = moves.count('U')
        D = moves.count('D')
        L = moves.count('L')
        R = moves.count('R')
        return True if U == D and L == R else False
