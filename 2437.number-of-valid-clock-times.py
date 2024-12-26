#
# @lc app=leetcode id=2437 lang=python
#
# [2437] Number of Valid Clock Times
#

# @lc code=start
class Solution(object):
    def countTime(self, time):
        """
        :type time: str
        :rtype: int
        """
        if '?' not in time:
            return 1
        choice = 1
        if time[0] == '?':
            if time[1] == '?' or time[1] < '4':
                choice *= 3
            else:
                choice *= 2
        if time[1] == '?':  
            choice *= 3
        if time[3] == '?':  
            choice *= 5
        if time[4] == '?':
            choice *= 10
        return choice
# @lc code=end

