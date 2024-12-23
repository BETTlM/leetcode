#
# @lc app=leetcode id=1893 lang=python
#
# [1893] Check if All the Integers in a Range Are Covered
#

# @lc code=start
class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        for i in range(left, right+1):
            if not any(left <= i <= right for left, right in ranges):
                return False
        return True
        
# @lc code=end

