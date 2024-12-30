#
# @lc app=leetcode id=2562 lang=python
#
# [2562] Find the Array Concatenation Value
#

# @lc code=start
class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        concat = 0
        while nums:
            if len(nums) != 1:
                c = int(str(nums.pop(0)) + str(nums.pop()))
                concat += c
            else:
                concat += nums.pop()
        return concat
        
# @lc code=end

