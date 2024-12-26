#
# @lc app=leetcode id=2427 lang=python
#
# [2427] Number of Common Factors
#

# @lc code=start
class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        commonFactors = 0 
        for i in range(1,min(a,b)+1):
            if a%i==0 and b%i==0:
                commonFactors += 1
        return commonFactors
# @lc code=end

