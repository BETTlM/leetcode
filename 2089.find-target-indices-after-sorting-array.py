#
# @lc app=leetcode id=2089 lang=python
#
# [2089] Find Target Indices After Sorting Array
#

# @lc code=start
class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexes = []
        sr = sorted(nums)
        for i in range(len(sr)):
            if sr[i] == target:
                indexes.append(i)
        return indexes

# @lc code=end

