class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        pos = [p for p, c in enumerate(S) if c == C]
        sl, sr = 0, 0 if len(pos)==1 else 1
        res = []
        for i in range(len(S)):
            if i > pos[sr] and i <= pos[-1] and len(pos) not in [1, 2]:
                sl, sr = sl+1, sr+1
            res.append(min(abs(pos[sl]-i), abs(pos[sr]-i)))
        return res