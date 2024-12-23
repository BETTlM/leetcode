#
# @lc app=leetcode id=1859 lang=python
#
# [1859] Sorting the Sentence
#

# @lc code=start
class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        retlist = []
        words = s.split()
        for i in range(len(words)):
            retlist.append(i)
        
        for i in words:
            retlist[int(i[-1])-1] = i[:-1]
        return ' '.join(retlist)
    
        
# @lc code=end

