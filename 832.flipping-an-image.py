#
# @lc app=leetcode id=832 lang=python
#
# [832] Flipping an Image
#

# @lc code=start
class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        returnImage = []
        for i in image:
            pixel = []
            for j in i[::-1]:
                if j == 1:
                    pixel.append(0)
                else:
                    pixel.append(1)
            returnImage.append(pixel)
        return returnImage
        
# @lc code=end

