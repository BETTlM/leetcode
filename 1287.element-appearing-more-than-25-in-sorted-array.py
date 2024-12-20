#
# @lc app=leetcode id=1287 lang=python
#
# [1287] Element Appearing More Than 25% In Sorted Array
#

# @lc code=start
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        tfp = len(arr) // 4
        max = 0
        nums = list(set(arr))
        for i in nums:
            if arr.count(i) > tfp:
                max = i
        
        return max
# @lc code=end

