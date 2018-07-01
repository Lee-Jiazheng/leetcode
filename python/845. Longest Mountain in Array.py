"""
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

 

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
 

Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
"""

class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        down = False
        max_len = 1; _len = 1; i = 0
        while i < len(A)-1:
            
            if not down and A[i+1]>A[i]:
                _len += 1
            elif ((not down and _len > 1) or down) and A[i+1] < A[i]:
                _len += 1; down = True
            else:
                max_len = max(max_len, _len) if down == True else max_len
                if down == True:
                    i = i - 1
                _len = 1; down = False
            i+=1
        if down == True:
            max_len = max(max_len, _len)
        return max_len if max_len != 1 else 0