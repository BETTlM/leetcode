#
# @lc app=leetcode id=520 lang=python
#
# [520] Detect Capital
#

# @lc code=start
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.istitle() or word.islower()
# @lc code=end

