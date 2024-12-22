#
# @lc app=leetcode id=1832 lang=python
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        return len(set(sentence)) == 26
        
# @lc code=end

