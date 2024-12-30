#
# @lc app=leetcode id=2553 lang=python
#
# [2553] Separate the Digits in an Array
#

# @lc code=start
class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        retlist = [] 
        for i in nums:
            if i<10:
                retlist.append(i)
            else:
                for j in str(i):
                    retlist.append(int(j))
        return retlist
# @lc code=end

