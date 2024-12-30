#
# @lc app=leetcode id=2788 lang=python
#
# [2788] Split Strings by Separator
#

# @lc code=start
class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        
        retlist = []
        for i in words:
            retlist.extend(i.split(separator))
        while ''  in retlist:
            retlist.remove('')
          
          

        return retlist
# @lc code=end

