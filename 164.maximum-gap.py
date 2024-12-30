#
# @lc app=leetcode id=164 lang=python
#
# [164] Maximum Gap
#

# @lc code=start
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snum = sorted(nums)
        max_gap = 0
        for i in range(len(snum)-1):
            max_gap = max(max_gap, snum[i+1] - snum[i])
        return max_gap
    
# @lc code=end

