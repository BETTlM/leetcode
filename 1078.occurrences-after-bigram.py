#
# @lc app=leetcode id=1078 lang=python
#
# [1078] Occurrences After Bigram
#

# @lc code=start
class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """

        ret = []
        words = text.split()
        for i in range(len(words)):
            if words[i] == first and words[i+1] == second and words[2+i] not in ret:
                ret.append(words[i+2])
        return ret
# @lc code=end

