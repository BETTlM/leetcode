#
# @lc app=leetcode id=2047 lang=python
#
# [2047] Number of Valid Words in a Sentence
#

# @lc code=start
class Solution(object):
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int
        """
        count = 0
        words = sentence.split()
        for i in words:
            status = True
            for j in i:
                if not j.isalpha():
                    status = False
                    break
            if status:
                count += 1
        return count
            
# @lc code=end

