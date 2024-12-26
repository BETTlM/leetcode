#
# @lc app=leetcode id=2490 lang=python
#
# [2490] Circular Sentence
#

# @lc code=start
class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        status = True
        sentence = sentence.split()
        if len(sentence) == 1:
            if sentence[0][0] != sentence[0][-1]:
                status = False
        else:
            for i in range(len(sentence)-1):
                if sentence[i][-1] != sentence[i+1][0]:
                    status = False
                    break
            if sentence[-1][-1] != sentence[0][0]:
                status = False

        return status
        
# @lc code=end

