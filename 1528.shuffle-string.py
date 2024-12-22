#
# @lc app=leetcode id=1528 lang=python
#
# [1528] Shuffle String
#

# @lc code=start
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        shuffled = [''] * len(s)
        for i in range(len(s)):
            shuffled[indices[i]] = s[i]
        return ''.join(shuffled)
# @lc code=end

