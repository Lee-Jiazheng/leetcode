# 要求时间为O(logn)
# 二分法查找上下界范围。

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def b_search(target):
            l, h = 0, len(nums)
            while l < h:
                mid = (l + h) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] >= target:
                    h = mid
            return l
        l = b_search(target)
        return [l, b_search(target+1)-1] if target in nums[l:l+1] else [-1, -1] # Think about when nums in []