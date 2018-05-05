class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = [0]*len(A)
        for i in range(1, len(A)-1):
            if A[i]-A[i-1] == A[i+1]-A[i]: dp[i]=dp[i-1]+1
        return sum(dp)        
            