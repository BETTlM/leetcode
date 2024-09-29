#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        templist = []
        indices = []
        count = 0
        for i in range(len(nums)):
            if nums[i] not in templist:
                templist.append(nums[i])
            else:
                count += 1
                indices.append(i)
        
        for i in indices:
            nums.pop(i)
            nums.append('_')
        
        return count

# @lc code=end

