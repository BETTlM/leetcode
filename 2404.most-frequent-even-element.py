#
# @lc app=leetcode id=2404 lang=python
#
# [2404] Most Frequent Even Element
#

# @lc code=start
class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_freq = -1
        for i in list(set(nums)):
            if i % 2 == 0:
                max_freq = max(max_freq, nums.count(i))
        return max_freq
        
# @lc code=end

