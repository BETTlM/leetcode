#
# @lc app=leetcode id=350 lang=python
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1)>len(nums2):
            minlist = nums2
        else:
            minlist = nums1
        
        inter = []
        for i in minlist:
            if i in nums1 and i in nums2:
                if inter.count(i)<min(nums1.count(i),nums2.count(i)):
                    inter.append(i)
            
        return inter
        
# @lc code=end

