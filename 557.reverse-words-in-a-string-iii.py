#
# @lc app=leetcode id=557 lang=python
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        rs = ''
        for i in s.split():
            rs += i[::-1]
            rs += ' '
        rs = rs[:-1:]
        return rs
        
# @lc code=end

