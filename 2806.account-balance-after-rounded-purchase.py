#
# @lc app=leetcode id=2806 lang=python
#
# [2806] Account Balance After Rounded Purchase
#

# @lc code=start
class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        if purchaseAmount%10 >= 5:
            purchaseAmount += 10 - purchaseAmount%10
        else:
            purchaseAmount -= purchaseAmount%10
        return 100 - purchaseAmount
# @lc code=end

