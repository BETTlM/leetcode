#
# @lc app=leetcode id=1979 lang=python
#
# [1979] Find Greatest Common Divisor of Array
#

# @lc code=start
class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num1,num2 = sorted(nums)[0], sorted(nums)[-1]
        maxdiv = 1
        for i in range(1, num1+1):
            if num1 % i == 0 and num2 % i == 0:
                maxdiv = i
        return maxdiv
# @lc code=end

