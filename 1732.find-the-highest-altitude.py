#
# @lc app=leetcode id=1732 lang=python
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = 0
        max_altitude = 0
        for g in gain:
            altitude += g
            max_altitude = max(max_altitude, altitude)
        return max_altitude
        
# @lc code=end

