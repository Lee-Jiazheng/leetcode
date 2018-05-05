class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        flags = [[True if i == j else False for i in range(len(s))] for j in range(len(s))]     # the window 1 is palindromic
        for i in range(len(s)-1):
            if s[i] == s[i+1]: flags[i][i+1] = True
        
        for k in range(3, len(s)+1):  # 窗口从3开始
            for i in range(0, len(s)-k+1):
                j = i + k - 1       # i, j是上下界; 
                if s[i] == s[j] and flags[i+1][j-1]:       # 如果中间是回文并且两边元素相同，那么他也是回文
                    flags[i][j] = True
        return sum([sum(flag) for flag in flags])