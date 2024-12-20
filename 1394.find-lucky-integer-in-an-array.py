#
# @lc app=leetcode id=1394 lang=python
#
# [1394] Find Lucky Integer in an Array
#

# @lc code=start
class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        current = -1
        for i in arr:
            if arr.count(i) == i:
                current = max(current, i)
        return current
# @lc code=end

