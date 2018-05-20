"""

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.

"""

# 循环的一个列表，设置一个stack用来保存ID，如果当前值大于栈顶的值，就一直弹，因为后面更大的值都是它。
# 最后再来一轮（循环数组）

class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        output = [-1]*len(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                output[stack.pop()] = nums[i]
            stack.append(i)
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                output[stack.pop()] = nums[i]
        return output