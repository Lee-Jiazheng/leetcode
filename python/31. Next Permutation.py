class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j = len(nums)-2, len(nums)-1
        while i>=0 and nums[i]>=nums[i+1]:
            i -= 1
        if i == -1: nums.reverse(); return
        
        while j>i and nums[j]<=nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]   # 说明前面一直是降序的，直接reverse就可以了