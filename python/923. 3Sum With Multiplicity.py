"""
Given an integer array A, and an integer target, return the number of tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.

 

Example 1:

Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
Example 2:

Input: A = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
 

Note:

3 <= A.length <= 3000
0 <= A[i] <= 100
0 <= target <= 300
"""

class Solution:
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        c = collections.Counter(A)
        res = 0
        for i, j in itertools.combinations_with_replacement(c, 2):
            # 顺序不变，不会出现(1,2)与(2,1)
            k = target - i - j
            if i == j == k:
                res += (c[i] * (c[i]-1) * (c[i]-2)) / (3*2*1)   # C_{N}^{3}
            elif i == j != k:
                res += (c[i] * (c[i]-1))/(2*1) * c[k]   # C_{N}^{2} * Nk
            elif k > i and k > j:
                print(i, j, k)
                res += c[i] * c[j] * c[k] 
            #print(res, i, j)
        return int(res % (1e9+7))
    