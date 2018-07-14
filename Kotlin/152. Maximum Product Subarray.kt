
// Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

// Example 1:

// Input: [2,3,-2,4]
// Output: 6
// Explanation: [2,3] has the largest product 6.
// Example 2:

// Input: [-2,0,-1]
// Output: 0
// Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

import kotlin.math.*

class Solution {
    fun maxProduct(nums: IntArray): Int {
        var imax = nums[0]
        var imin = nums[0]
        var r = nums[0]
        for (num in nums.slice(1 until nums.size)) {
            if (num < 0) {
                var temp = imax
                imax = imin
                imin = temp
            }

            imax = max(num, imax*num)   // 如果imax*num比num还要小，那么截取的子array是从当前num开始的
            imin = min(num, imin*num)   // 找到一个最小的数，防止后面有负数相乘得到大的

            r = max(r, imax)
            println("$num, $imax, $imin, $r")
        }
        return r
    }
}