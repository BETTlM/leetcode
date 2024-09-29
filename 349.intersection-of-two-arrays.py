#
# @lc app=leetcode id=349 lang=python
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1)>len(nums2):
            minlist = nums2
        else:
            minlist = nums1
        
        intersection = []
        for i in minlist:
            if i in nums1 and i in nums2:
                if i not in intersection:
                    intersection.append(i)
        return intersection
# @lc code=end

