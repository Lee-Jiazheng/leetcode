"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1

Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, h = 0, len(nums)-1
        # 使用数字进行判断，更快结束
        while nums[l] > nums[h]:
            mid = (l+h) // 2
            if nums[mid] < nums[h]:
                h = mid
            elif nums[mid] > nums[h]:
                l = mid + 1
            else:
                # 提前终止
                return nums[l]
        return nums[l]