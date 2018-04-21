class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        _res = []
        for x in nums:
            if nums[abs(x)-1] < 0: _res.append(abs(x))
            else: nums[abs(x)-1] *= -1
        return _res         # 每个数字都在1<=a[i]<=n，所以出现对应数字就把对应位置设为负数作为标记，节省空间。
    
    def findDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = {}; _res = []
        for n in nums:
            if n not in res: res[n] = True
            else: _res.append(n)
        return _res