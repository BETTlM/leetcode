#
# @lc app=leetcode id=884 lang=python
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        s1=s1.split()
        s2=s2.split()
        ref = max(s1,s2)
        temp = min(s1,s2)
        ret = []
        for i in ref:
            if i not in temp and s1.count(i)+s2.count(i)==1:
                ret.append(i)
        for i in temp:
            if i not in ref and s1.count(i)+s2.count(i)==1:
                ret.append(i)

        return ret
    
        
# @lc code=end

