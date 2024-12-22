#
# @lc app=leetcode id=1619 lang=python
#
# [1619] Mean of Array After Removing Some Elements
#

# @lc code=start
class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        twenty = len(arr) // 20
        newarr = sorted(arr)
        newarr = newarr[twenty:-twenty]
        return sum(newarr) / len(newarr)
# @lc code=end

