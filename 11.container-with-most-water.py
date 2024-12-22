#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            width = right - left
            maxarea = max(maxarea, width * min(height[left], height[right]))
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxarea
# @lc code=end

