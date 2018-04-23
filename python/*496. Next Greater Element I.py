# 设置一个栈
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        A = {}; stack = []
        for num in nums2:
            while(len(stack) and stack[-1] < num):
                A[stack.pop()] = num
            stack.append(num)
        for i, num in enumerate(nums1):
            nums1[i] = A.get(num, -1)
        return nums1
            