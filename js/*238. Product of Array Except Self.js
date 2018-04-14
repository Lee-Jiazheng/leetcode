/**
 * Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
 */


 /**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    result = [1]
    for (var i = 1; i < nums.length; ++i) {
        result[i] = result[i-1] * nums[i-1]
    }
    console.log(result)
    right = 1
    for (var i = nums.length - 1; i >= 0; --i) {
        result[i] = result[i]*right
        right *= nums[i]
    }
    return result
};