class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        Rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        res = []
        for tword in words:
            word = tword.lower()
            row = None
            ok = None
            for i in range(len(Rows)):
                if word[0] in Rows[i]:
                    row = i
                    break
            for i in range(1, len(word)):
                if word[i] not in Rows[row]:
                    ok = False
                    break
            if ok != False:
                res.append(tword)
                
        return res
