#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#

# @lc code=start
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        seen = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                left = j+1
                right = len(nums)-1
                while left < right:
                    sum_ = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum_ == target:
                        if (nums[i], nums[j], nums[left], nums[right]) not in seen:
                            result.append([nums[i], nums[j], nums[left], nums[right]])
                            seen.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif sum_ < target:
                        left += 1
                    else:
                        right -= 1
        return result
    
        
# @lc code=end

