class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = None
        maxcount = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                if count > maxcount:
                    maxcount = count
                count = 0
        maxcount = (count > maxcount) ? count : maxcount
            maxcount = count
        return maxcount
            
        
