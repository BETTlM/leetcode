#
# @lc app=leetcode id=2540 lang=python
#
# [2540] Minimum Common Value
#

# @lc code=start
class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums2_set = set(nums2)
        for i in nums1:
            if i in nums2_set:
                return i
        return -1
            
# @lc code=end

