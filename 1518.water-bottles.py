#
# @lc app=leetcode id=1518 lang=python
#
# [1518] Water Bottles
#

# @lc code=start
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        drinkable = numBottles
        empty = numBottles
        while empty >= numExchange:
            drinkable += empty // numExchange
            empty = empty // numExchange + empty % numExchange
        return drinkable
    
# @lc code=end

