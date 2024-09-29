#
# @lc app=leetcode id=485 lang=python
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        summ = 0

        for num in nums:
            if num == 0:
                summ = 0
            else:
                summ += num
                ans = max(ans, summ)

        return ans   
# @lc code=end

