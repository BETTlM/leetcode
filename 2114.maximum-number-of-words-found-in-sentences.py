#
# @lc app=leetcode id=2114 lang=python
#
# [2114] Maximum Number of Words Found in Sentences
#

# @lc code=start
class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        maxn = 0 
        for i in sentences:
            maxn = max(maxn , len(i.split()))
        return maxn
        
# @lc code=end

