#
# @lc app=leetcode id=976 lang=python
#
# [976] Largest Perimeter Triangle
#

# @lc code=start
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0 

        
# @lc code=end

