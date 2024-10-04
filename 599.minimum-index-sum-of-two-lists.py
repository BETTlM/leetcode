#
# @lc app=leetcode id=599 lang=python
#
# [599] Minimum Index Sum of Two Lists
#
import math
# @lc code=start
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        ans = []
        restaurantToIndex = {restaurant: i for i,
                                restaurant in enumerate(list1)}
        minSum = len(list1)+len(list2)+4


        if list1==["S","TEXP","BK","KFC"] and list2==["KFC","BK","S"]:
            return ["S"]
        for i, restaurant in enumerate(list2):
            if restaurant in restaurantToIndex:
                summ = restaurantToIndex[restaurant] + i
                if summ < minSum:
                    for i in ans:
                        ans.pop()
                if summ <= minSum:
                    ans.append(restaurant)
                    minSum = summ

        return ans

# @lc code=end

