# dfs
# 找到多少个朋友圈子
# 顺着一个找把M的对应圈子设为0。
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(len(M)):
            if M[i][i] == 1:
                self.dfs(M, i)
                count += 1
        return count
    
    def dfs(self, M, i):
        for j in range(len(M)):
            if M[i][j] == 1:
                M[i][j] = M[j][i] = 0
                self.dfs(M, j)