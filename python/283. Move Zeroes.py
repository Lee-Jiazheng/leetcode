# 不能改变nums的地址，即新建变量， 48ms, 99.3%

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums1 = list(filter(lambda x: x != 0, nums))
        nums[:len(nums1)] = nums1
        nums[len(nums1):] = [0] * (len(nums) - len(nums1))
