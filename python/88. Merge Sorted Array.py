"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
# 重点在于指针从后向前，直接预留出位置，把大的方后面，还不会影响nums1数组
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        im, i2 = m-1, n-1
        i = m + n - 1
        while im>=0 or i2>=0:
            if im < 0: nums1[:i+1] = nums2[:i2+1]; break
            elif i2 < 0: nums2[:i+1] = nums1[:im+1]; break
            elif nums1[im] > nums2[i2]: nums1[i] = nums1[im]; im -= 1
            else: nums1[i] = nums2[i2]; i2 -= 1
            i -= 1
            
            