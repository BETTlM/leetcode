#
# @lc app=leetcode id=2278 lang=python
#
# [2278] Percentage of Letter in String
#

# @lc code=start
class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        counts = s.count(letter)
        percentage = int((counts / len(s)) * 100)
        return percentage
# @lc code=end

