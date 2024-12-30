#
# @lc app=leetcode id=2824 lang=python
#
# [2824] Count Pairs Whose Sum is Less than Target
#

# @lc code=start
class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0 
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] < target:
                    count += 1
        return count
# @lc code=end

