#
# @lc app=leetcode id=434 lang=python
#
# [434] Number of Segments in a String
#

# @lc code=start
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
# @lc code=end

