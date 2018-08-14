"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""

# 如果第一个位置的元素和最后一个位置的元素不能同时选择，
# 那么改变策略，找到前面的（不含最后一个元素）的结果，找到后面的结果，取最大值即可
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) < 4: return max(nums)
        n1, n2 = nums[:], nums[:]
        return max(self.find(n1, 1, len(nums)), self.find(n2, 0, len(nums)-1))
    
    def find(self, nums, l, r):
        nums[l+1] = max(nums[l], nums[l+1]) 
        for i in range(l+2, r):
            nums[i] = max(nums[i-2]+nums[i], nums[i-1])
        return nums[r-1]