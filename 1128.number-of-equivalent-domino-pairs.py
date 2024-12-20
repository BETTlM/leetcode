#
# @lc app=leetcode id=1128 lang=python
#
# [1128] Number of Equivalent Domino Pairs
#

# @lc code=start
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        count = 0
        freq = {}

        for domino in dominoes:
            normalized = tuple(sorted(domino))
            if normalized in freq:
                count += freq[normalized]
                freq[normalized] += 1
            else:
                freq[normalized] = 1

        return count

# @lc code=end

