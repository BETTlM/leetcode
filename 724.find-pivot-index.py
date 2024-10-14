#
# @lc app=leetcode id=724 lang=python
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        for i in range(len(nums)):
                leftsum=sum(nums[:i])
                rightsum = sum(nums[i+1:])

                if rightsum == leftsum:
                    return i
        return -1

# @lc code=end

