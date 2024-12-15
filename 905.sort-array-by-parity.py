#
# @lc app=leetcode id=905 lang=python
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        even.extend(odd)
        return even
# @lc code=end

