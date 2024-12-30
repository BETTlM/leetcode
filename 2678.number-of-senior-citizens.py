#
# @lc app=leetcode id=2678 lang=python
#
# [2678] Number of Senior Citizens
#

# @lc code=start
class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        boomers = 0 
        for i in details:
            if int(i[-4:-2]) > 60:
                boomers += 1
        return boomers
# @lc code=end

