# 主要是题目理解比较难
# https://yq.aliyun.com/articles/889 图片一目了然

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        water = 0
        while left < right:
            water = max(water, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return water