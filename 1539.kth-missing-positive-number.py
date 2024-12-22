#
# @lc app=leetcode id=1539 lang=python
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        count = 0 
        for i in range(1, arr[-1] + k + 1):
            if i not in arr:
                count += 1
            if count == k:
                return i
# @lc code=end

