class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dt = {}
        for i, num in enumerate(nums):
            if target - num in dt:
                return [dt[target-num], i]
            dt[num] = i