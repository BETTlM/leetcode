#
# @lc app=leetcode id=1941 lang=python
#
# [1941] Check if All Characters Have Equal Number of Occurrences
#

# @lc code=start
class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = s.count(s[0])
        return all(s.count(c) == count for c in s)
    
# @lc code=end

