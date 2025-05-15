#
# @lc app=leetcode id=1524 lang=python
#
# [1524] Number of Sub-arrays With Odd Sum
#

# @lc code=start
class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                subarray = arr[i:j+1]
                sumofsub = sum(subarray)
                if sumofsub % 2 == 1:
                    count += 1
        return count
# @lc code=end

