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
        index = 0
        length = len(nums)

        while index<length:
            if nums[index]==0:
                nums.pop(int(index-displacement))
                displacement-=1
                length=length-1
            index = index + 1
            
# @lc code=end

