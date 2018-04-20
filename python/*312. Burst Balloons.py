"""
* Hard!!! https://leetcode.com/problems/burst-balloons/description/

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""

"""
采用动态规划的方法，
由于爆破一个气球会影响下一次的分值计算，所以我们采用Bottom up的形式，
首先找到最后一个爆破的气球，计算可能的分值。
因为只有三个气球的时候才能计算分数，所以k从2开始计算。
left, right = 0, 2的时候，dp[0][2] = nums[0]*nums[1]*nums[2], 针对每个间隔可能爆破的气球都计算一次，0/2中间只有1.
left, right = 0, 4的时候， dp[0][4] 需要找到0到4之间最大的点(i)。
nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right]代表：
前一项是爆破本次气球应得分数
中间是爆破本次气球前左侧得分
后一项是爆破本次气球前，右侧得分。

dp[i][j]代表爆破i到j得分最高值。
"""
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + [num for num in nums if num > 0] + [1]     # num == 0 is not necessary
        dp = [[0] * len(nums) for _ in range(len(nums))]
        
        for k in range(2, len(nums)):
            for left in range(0, len(nums) - k):
                right = left + k
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
                print(left, right, dp[left][right])
        print(dp)
        return dp[0][len(nums)-1]
            