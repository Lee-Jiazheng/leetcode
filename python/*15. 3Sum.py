class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        _nums = {}
        # Counter 速度慢
        for n in nums:
            if n not in _nums:
                _nums[n] = 1
            else:
                _nums[n] = _nums[n] + 1
                
        n_s = list(set(nums))
        n_s.sort()
        
        for i, n1 in enumerate(n_s):
            _nums[n1] = _nums[n1] - 1
            for j, n2 in enumerate(n_s[i:]):
                if _nums[n2] == 0: continue
                n3 = -(n1+n2)
                if n3 >= n2 and _nums.get(n3, 0) > (1 if n2 == n3 else 0):
                    res.add((n1, n2, n3))
            _nums[n1] = _nums[n1] + 1
        return list(res)