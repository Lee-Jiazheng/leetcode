# 硬解
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.combine(candidates, target)
        return self.res
        
                
    
    def combine(self, candidates, target, path=[]):
        if target < 0:
            return None
        elif target == 0:
            path = sorted(path)
            if path not in self.res:
                self.res.append(sorted(path))
        else:
            [self.combine(candidates, target-c, path+[c]) for c in candidates]



## 剪枝!!!
## start的作用：
## 当以第2个数开头的时候，不会出现第一个数
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.combine(candidates, target)
        return self.res
        
                
    
    def combine(self, candidates, target, path=[], start=0):
        if target < 0:
            return None
        elif target == 0:
            self.res.append(path)
        else:
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                self.combine(candidates, target-candidates[i], path+[candidates[i]], i)
                
