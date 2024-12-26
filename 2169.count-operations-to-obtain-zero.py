#
# @lc app=leetcode id=2169 lang=python
#
# [2169] Count Operations to Obtain Zero
#

# @lc code=start
class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        moves = 0
        while num1 != 0 and num2 != 0:
            if num1 > num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
            moves += 1
        return moves
         
            
            # @lc code=end

