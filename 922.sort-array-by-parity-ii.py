#
# @lc app=leetcode id=922 lang=python
#
# [922] Sort Array By Parity II
#

# @lc code=start
class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        length = len(even) + len(odd)
        retlist = []
        for i in range(length):
            if i%2==0:
                retlist.append(even[i//2])
            else:
                retlist.append(odd[(i-1)//2])
        return retlist
        
# @lc code=end

