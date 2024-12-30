#
# @lc app=leetcode id=2605 lang=python
#
# [2605] Form Smallest Number From Two Digit Arrays
#

# @lc code=start
class Solution(object):
    def minNumber(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1.sort()
        nums2.sort()
        for i in nums1:
            if i in nums2:
                return i 
        
        return int(str(nums1[0]) + str(nums2[0])) if nums1[0] < nums2[0] else int(str(nums2[0]) + str(nums1[0]))
    
        
# @lc code=end

