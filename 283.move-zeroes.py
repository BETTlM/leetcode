#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        displacement = 0
        length = len(nums)
        for i in range(length):
            if nums[i] == 0:
                nums.pop(i)
                length = length - 1
                displacement = displacement + 1
                nums.append(0)

            
# @lc code=end

