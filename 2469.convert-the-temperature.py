#
# @lc app=leetcode id=2469 lang=python
#
# [2469] Convert the Temperature
#

# @lc code=start
class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        faranheit = celsius * 1.80 + 32
        kelvin = celsius + 273.15
        return [kelvin, faranheit]
        
# @lc code=end

