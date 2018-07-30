"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:

Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:

Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.

Note: The n belongs to [1, 10,000]. 
"""

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] >= nums[i-1]: continue
            cnt += 1
            # 考虑前2个数，如果它比当前数大，但是它比前一个数小，
            # 那么不能随便改，改成与前一个数相同的数字，不会对后面序列产生影响
            if i >= 2 and nums[i-2] >= nums[i]:
                nums[i] = nums[i-1]
            else:
                nums[i-1] = nums[i]
        
        return cnt <= 1