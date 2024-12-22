#
# @lc app=leetcode id=1668 lang=python
#
# [1668] Maximum Repeating Substring
#

# @lc code=start
class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        count = 0
        while word*(count+1) in sequence:
            count += 1
        return count
        
# @lc code=end

