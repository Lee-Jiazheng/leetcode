class Solution:
    
    def __init__(self):
        self.final = 0
    def depth(self, ele, d):  
        if list(ele.keys()) == ["selected"]: self.final += d; 
        else: 
            if "selected" in ele: del ele["selected"]
            return [self.depth(e, d+1) for e in ele.values()]
    
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = {}
        for word in words:
            tp = res
            for c in word[::-1]:
                if c not in tp: tp[c] = {}
                tp = tp[c]
            tp["selected"] = tp.get("selected", 0) + 1
        self.depth(res, 1)
        return self.final
    