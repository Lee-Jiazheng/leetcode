"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

"""

# *python time limit excedded
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        cans = [x**2 for x in range(1, int(math.sqrt(n))+1)]
        cal = [float('inf') for _ in range(n+1)]
        cal[0] = 0
        for i in range(1, n+1):
            for c in cans:
                if i - c >= 0:
                    cal[i] = min(cal[i], 1+cal[i-c])
                else:
                    break
        return cal[-1]
        
        for i in range(1, n+1):
            m = -1
            for j in range(1, i+1):
                if i - cans[j] < 0: break
                cur = cal[i-cans[j]] + 1  
                if cur < m or m == -1:
                    m = cur
            cal[i] = m
        return cal[n]