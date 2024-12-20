#
# @lc app=leetcode id=1207 lang=python
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occurences = []
        for i in list(set(arr)):
            o = arr.count(i)
            if o not in occurences:
                occurences.append(o)
            else:
                return False
        return True

        
# @lc code=end

