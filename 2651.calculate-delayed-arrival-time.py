#
# @lc app=leetcode id=2651 lang=python
#
# [2651] Calculate Delayed Arrival Time
#

# @lc code=start
class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        return (arrivalTime + delayedTime ) % 24
        
# @lc code=end

