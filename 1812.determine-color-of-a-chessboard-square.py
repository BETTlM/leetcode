#
# @lc app=leetcode id=1812 lang=python
#
# [1812] Determine Color of a Chessboard Square
#

# @lc code=start
class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        c = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        return (c[coordinates[0]] + int(coordinates[1])) % 2 != 0
    
        
# @lc code=end

