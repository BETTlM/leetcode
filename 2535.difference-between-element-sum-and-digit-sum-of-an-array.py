#
# @lc app=leetcode id=2535 lang=python
#
# [2535] Difference Between Element Sum and Digit Sum of an Array
#

# @lc code=start
class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = 0
        for i in nums:
            for j in str(i):
                sum1 += int(j)
        return abs(sum(nums) - sum1)
# @lc code=end

