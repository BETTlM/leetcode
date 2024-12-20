#
# @lc app=leetcode id=1089 lang=python
#
# [1089] Duplicate Zeros
#

# @lc code=start
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        for i in range(len(arr)):
            if arr[i] == 0:
                arr.insert(i,0)
                arr.pop()
# @lc code=end

