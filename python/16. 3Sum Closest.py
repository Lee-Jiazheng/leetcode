class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        print(nums)
        rec = (float("inf"), 0)
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                _sum = nums[i] + nums[l] + nums[r]
                _diff = min(abs(_sum - target), rec[0])
                if _diff == 0:
                    return _sum
                elif _sum > target:
                    r -= 1
                else:
                    l += 1
                rec = (_diff, _sum) if _diff < rec[0] else rec
        return rec[1]