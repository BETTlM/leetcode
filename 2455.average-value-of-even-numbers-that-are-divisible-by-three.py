#
# @lc app=leetcode id=2455 lang=python
#
# [2455] Average Value of Even Numbers That Are Divisible by Three
#

# @lc code=start
class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        divis3 = []
        for i in nums:
            if i % 3 == 0 and i % 2 == 0:
                divis3.append(i)
        if not divis3:
            return 0
        return sum(divis3) / len(divis3)
        
# @lc code=end

