#
# @lc app=leetcode id=1431 lang=python
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        for i in candies:
            if i + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result
# @lc code=end

