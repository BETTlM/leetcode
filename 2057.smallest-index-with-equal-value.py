#
# @lc app=leetcode id=2057 lang=python
#
# [2057] Smallest Index With Equal Value
#

# @lc code=start
class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = -1
        for i in range(len(nums)):
            if i%10 == nums[i]:
                result = i
                break
        return result
# @lc code=end

