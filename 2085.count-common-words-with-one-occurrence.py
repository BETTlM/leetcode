#
# @lc app=leetcode id=2085 lang=python
#
# [2085] Count Common Words With One Occurrence
#

# @lc code=start
class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        count = 0
        for i in words1:
            if i in words2 and words1.count(i) == 1 and words2.count(i) == 1:
                count += 1
        return count
        
# @lc code=end

