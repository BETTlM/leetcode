#
# @lc app=leetcode id=229 lang=python
#
# [229] Majority Element II
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numnum = []
        unique = list(set(nums))
        for i in unique:
            if nums.count(i) > len(nums) // 3:
                numnum.append(i)
        return numnum     
# @lc code=end

